import gym
from gym import spaces
import numpy as np
from stable_baselines.common.env_checker import check_env
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common import make_vec_env
from stable_baselines import PPO2
from env import CustomEnv
from data_formatting import clean_data

"""
This file is used to evaluate the model.
"""

def infected_policy(state):
    
    
def infected_policy_reward(env, action):
    
    
def population_policy(state):
    
    
def population_policy_reward(env, action):


def learned_policy_reward(env, action,model_path):


def rewards_from_policy(env,action,steps,efficacy,model_path): #This is all we need to call


if __name__ == "__main__": #Just to test results
    x=0