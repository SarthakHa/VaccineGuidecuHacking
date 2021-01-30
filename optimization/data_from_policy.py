import gym
from gym import spaces
import numpy as np
from stable_baselines.common.env_checker import check_env
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common import make_vec_env
from stable_baselines import PPO2
import sys
sys.path.append('./optimization')
from model import PlaceModel
from env import CustomEnv

def data_from_policy(env,policy_path):
    """
    INPUT PARAMETERS:
    ----------------
    env : gym.Env
        The environment curated by gym

    policy_path : str
        The path to the file of the policy
    """
    