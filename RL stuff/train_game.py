from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import time

import tensorflow as tf
from absl import flags, app
from absl import logging
from tf_agents.agents.ppo import ppo_agent
from tf_agents.drivers import dynamic_episode_driver
from tf_agents.environments import parallel_py_environment
from tf_agents.environments import tf_py_environment
from tf_agents.metrics import tf_metrics
from tf_agents.networks.actor_distribution_network import ActorDistributionNetwork
from tf_agents.networks.value_network import ValueNetwork
from tf_agents.replay_buffers import tf_uniform_replay_buffer
import numpy as np
from env import VaccineEnvironment

def create_networks(observation_spec, action_spec):
	actor_net = ActorDistributionNetwork(
		observation_spec,
		action_spec,
		activation_fn=tf.nn.relu)
	value_net = ValueNetwork(
		observation_spec,
		activation_fn=tf.nn.relu)

	return actor_net, value_net


def train_eval_vaccine_simple(
		# Params for collect
		num_environment_steps=180,
		collect_episodes_per_iteration=2,
		num_parallel_environments=1,
		replay_buffer_capacity=301,  # Per-environment
		# Params for train
		num_epochs=50,
		learning_rate=4e-4,
		# Params for eval
		eval_interval=10,
		# Params for summaries and logging
		log_interval=50):
	initial_states = np.array([[6185501.0,177589.0,360087.0,8823.0],[6435833.0,254866.0,38445.0,2856.0],[6028735.0,172488.0,513383.0,17394.0]])
	total_populations = np.array([673200,4500000,12700000])
	params = np.array([[0,0.0369,0.0228,0.000387],[0.002158,0.03058,0.002921,0.0002043],[0.0,0.029299,0.01911,0.000444]])
	eval_py_env = VaccineEnvironment(initial_states,params,total_populations,200000)
	eval_tf_env = tf_py_environment.TFPyEnvironment(eval_py_env)
	tf_env = tf_py_environment.TFPyEnvironment(parallel_py_environment.ParallelPyEnvironment([VaccineEnvironment] * num_parallel_environments))

	actor_net, value_net = create_networks(tf_env.observation_spec(), tf_env.action_spec())

	global_step = tf.compat.v1.train.get_or_create_global_step()
	optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate, epsilon=1e-5)

	tf_agent = ppo_agent.PPOAgent(
		tf_env.time_step_spec(),
		tf_env.action_spec(),
		optimizer,
		actor_net,
		value_net,
		num_epochs=num_epochs,
		train_step_counter=global_step,
		discount_factor=1,
		gradient_clipping=0.5,
		entropy_regularization=1e-2,
		importance_ratio_clipping=0.2,
		use_gae=True,
		use_td_lambda_return=True
	)
	tf_agent.initialize()

	environment_steps_metric = tf_metrics.EnvironmentSteps()
	step_metrics = [
		tf_metrics.NumberOfEpisodes(),
		environment_steps_metric,
	]

	replay_buffer = tf_uniform_replay_buffer.TFUniformReplayBuffer(tf_agent.collect_data_spec, batch_size=num_parallel_environments, max_length=replay_buffer_capacity)
	collect_driver = dynamic_episode_driver.DynamicEpisodeDriver(tf_env, tf_agent.collect_policy, observers=[replay_buffer.add_batch] + step_metrics, num_episodes=collect_episodes_per_iteration)


	def train_step():
		trajectories = replay_buffer.gather_all()
		return tf_agent.train(experience=trajectories)


	def evaluate():
		print("hi")


	collect_time = 0
	train_time = 0
	timed_at_step = global_step.numpy()

	while environment_steps_metric.result() < num_environment_steps:

		start_time = time.time()
		collect_driver.run()
		collect_time += time.time() - start_time

		start_time = time.time()
		total_loss, _ = train_step()
		replay_buffer.clear()
		train_time += time.time() - start_time

		global_step_val = global_step.numpy()

		if global_step_val % log_interval == 0:
			logging.info('step = %d, loss = %f', global_step_val, total_loss)
			steps_per_sec = ((global_step_val - timed_at_step) / (collect_time + train_time))
			logging.info('%.3f steps/sec', steps_per_sec)
			logging.info('collect_time = {}, train_time = {}'.format(collect_time, train_time))

			timed_at_step = global_step_val
			collect_time = 0
			train_time = 0

		if global_step_val % eval_interval == 0:
			evaluate()

	evaluate()


def main(_):
	tf.compat.v1.enable_v2_behavior()  # For TF 1.x users
	logging.set_verbosity(logging.INFO)
	train_eval_vaccine_simple()


if __name__ == '__main__':
	app.run(main)
