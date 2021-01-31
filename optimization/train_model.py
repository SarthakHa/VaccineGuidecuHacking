import gym
from gym import spaces
import os,subprocess
import copy
import numpy as np
from stable_baselines.common.env_checker import check_env
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common import make_vec_env
from stable_baselines import PPO2
from data_formatting import clean_data
from stable_baselines.bench import Monitor
from stable_baselines.results_plotter import load_results, ts2xy
from stable_baselines.common.callbacks import BaseCallback
from stable_baselines.common.callbacks import CheckpointCallback
from stable_baselines import SAC
from stable_baselines.common.vec_env import DummyVecEnv, VecNormalize
from stable_baselines.common.vec_env import SubprocVecEnv


import tensorflow as tf
from model import PlaceModel
from env import CustomEnv

#code modified from stable_baselines examples:https://stable-baselines.readthedocs.io/en/master/guide/examples.html#examples
class SaveBest(BaseCallback):
    def __init__(self, sample_rate, path, verbose=1):
        super(SaveBest, self).__init__(verbose)
        self.sample_rate = sample_rate
        self.path = path
        self.save_path = os.path.join(path, 'best_model')
        self.best = -np.inf

    def _on_step(self) -> bool:
        if self.n_calls % self.sample_rate == 0:
          x, y = ts2xy(load_results(self.path), 'timesteps')
          if len(x) > 0:
              mean_reward = np.mean(y[-100:])
              if mean_reward > self.best:
                  self.best = mean_reward
                  self.model.save(self.save_path)

        return True

def train_agent(env,learning_rate,total_episodes,path,port):
    cb = SaveBest(100, path=path)
    def _make_env():
        return copy.deepcopy(env)
    #train_env = SubprocVecEnv([_make_env for _ in range(4)])
    #train_env = VecNormalize(train_env, norm_obs=True, norm_reward=False)
    env = Monitor(env, path)

    tensorboard_path = "."+path+"/log/"
    policy_kwargs = dict(net_arch=[5,5])


    model = PPO2(MlpPolicy, env,policy_kwargs=policy_kwargs,tensorboard_log=tensorboard_path,gamma=1.0,nminibatches =2)

    cmd_str = "tensorboard --logdir " + tensorboard_path + " --port=" + str(port)
    print(cmd_str)
    p = subprocess.Popen(cmd_str.split(" "))

    print(total_episodes*env.max_steps)
    model.learn(total_timesteps=total_episodes*env.max_steps,callback=cb)
    model.save(path+"/ppo2_vaccine")

    p.kill()

if __name__ == "__main__": #Just to test
    place_names,params,total_populations,initial_states = clean_data(np.load("/home/steelshot/nwHacksVaccDistr/model_fitting/data/tests.npy",allow_pickle=True))
    env = CustomEnv(params,initial_states,total_populations,500000,180,place_names,0.95)

    train_agent(env,0.0003,10000,"/home/steelshot/nwHacksVaccDistr/optimization/models")


