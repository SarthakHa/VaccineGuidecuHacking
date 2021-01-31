import numpy as np
import matplotlib as plt

def aggregate_state(state):
    

def infected_policy(state):
    infected_data = []
    for i in range(len(state)):
        if i%4 == 1:
            infected_data.append(state[i])
    return (infected_data,[])

def population_policy(population):
    return population,[]

def infected_policy_reward(env, action):
    obs = env.reset()
    dones = False
    total_reward = 0
    while not dones:
        action, _states = infected_policy(obs)
        obs, reward, dones, info = env.step(action)
        total_reward += reward
    return total_reward

def population_policy_reward(env, action):
    obs = env.reset()
    dones = False
    reward = 0
    while not dones:
        action, _states = population_policy(env.total_populations)
        obs, rewards, dones, info = env.step(action)
        reward += rewards
    return reward

def learned_policy_reward(env, action,model_path):
    model = PPO2.load(model_path)
    obs = env.reset()
    dones = False
    reward = 0
    while not dones:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        reward += rewards

