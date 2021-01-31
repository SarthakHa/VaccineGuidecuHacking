import gym
from gym import spaces
import numpy as np
from stable_baselines.common.env_checker import check_env
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common import make_vec_env
from stable_baselines import PPO2

from model import PlaceModel
from env import CustomEnv
from data_formatting import clean_data

def data_from_policy(env,policy_path):
    model = PPO2.load(policy_path)
    actions = []
    states = dict()
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
    return [obsloop, actions]
#Observations per day, vaccine distributions

if __name__ == "__main__": #Just to test
    place_names,params,total_populations,initial_states = clean_data(np.load("/home/steelshot/nwHacksVaccDistr/optimization/model_fitting/data/tests.npy",allow_pickle=True))
    env = CustomEnv(params,initial_states,total_populations,100000,180,place_names,0.95)
    d = data_from_policy(env,'models/ppo2_vaccine')
    np.save("data.npy",d)
