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
This file is used to evaluate the model for the different policies.
"""

def infected_policy(state):
    infected_data = []
    for i in range(len(state)):
        if i%4 == 1:
            infected_data.append(state[i])
    return (infected_data,[])
    
def infected_policy_reward(env, action):
    obs = env.reset()
    dones = False
    total_reward = 0
    while not dones:
        action, _states = infected_policy(obs)
        obs, reward, dones, info = env.step(action)
        total_reward += reward
    return total_reward
    
def population_policy(population):
    return population,[]
    
def population_policy_reward(env, action):
    obs = env.reset()
    dones = False
    reward = 0
    while not dones:
        action, _states = population_policy([0]*5)
        obs, rewards, dones, info = env.step(action)
        reward += rewards
    return reward

def learned_policy_reward(env,action,model_path):
    model = PPO2.load(model_path)
    obs = env.reset()
    dones = False
    reward = 0
    while not dones:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        reward += rewards
    return reward

def rewards_from_policy(env,action,steps,efficacy,model_path): #This is all we need to call
    infected_reward = infected_policy_reward(env,action)
    population_reward = population_policy_reward(env,action)
    learned_reward = learned_policy_reward(env,action,model_path)
    return [infected_reward, population_reward, learned_reward]

if __name__ == "__main__": #Just to test results
    place_names,params,total_populations,initial_states = clean_data(np.load("model_fitting/test_data/data.npy",allow_pickle=True))
    env = CustomEnv(params,initial_states,total_populations,100000,180,place_names,0.95)

    infect_reward = infected_policy_reward(env,100000)
    population_reward = population_policy_reward(env,100000)
    learned_reward = learned_policy_reward(env,100000,"ppo2_cartpole")

    print("Reward from infected ratio policy:", infect_reward)
    print("Reward from population ratio policy:", population_reward)
    print("Reward from learned policy:", learned_reward)