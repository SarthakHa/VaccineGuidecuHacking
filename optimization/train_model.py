import gym
from gym import spaces
import os,subprocess
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
import tensorflow as tf
from model import PlaceModel
from env import CustomEnv

#code modified from stable_baselines examples:https://stable-baselines.readthedocs.io/en/master/guide/examples.html#examples

def train_agent(env,learning_rate,total_episodes,path,port):
    cb = SaveBest(100, path=path)
    env = Monitor(env, path)

    model = PPO2(MlpPolicy, env, verbose=1,policy_kwargs = policy_kwargs,tensorboard_log=tensorboard_path,gamma=1.0,n_steps=128,learning_rate=learning_rate)
    

    model.learn(total_timesteps=total_episodes*env.max_steps,callback=cb)
    model.save(path+"/ppo2_vaccine")

    p.kill()



