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
    env : gym.Env (class environment)
        The environment curated by gym

    policy_path : str
        The path to the file of the policy
    """
    model = PPO2.load(policy_path)
    actions = []
    states = {}
    for place in env.place_names:
        states[place] = []
    obs = env.reset()
    dones = False
    reward = 0
    obsloop = {}

    for place in env.place_names:
        obsloop[place] = []

    while not dones:
        action, _states = model.predict(obs,deterministic=True)
    
        actions.append(env.vaccines_per_day*(action/sum(action)))
        obs, rewards, dones, info = env.step(action)
        reward += rewards
        #savedobs.append(obs.reshape((len(env.place_names),4)))
        for place in env.place_names:
            obsloop[place].append(obs.reshape((len(env.place_names),4))[np.where(env.place_names==place)[0]])
    return [obsloop, actions]#Observations per day, vaccine distributions