import gym
from gym import spaces
import numpy as np
from stable_baselines.common.env_checker import check_env
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common import make_vec_env
from stable_baselines import PPO2
from env import CustomEnv
from data_formatting import clean_data
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TKAGG")


def infected_policy(state):
    infected_data = []
    for i in range(len(state)):
        if i%4 == 1:
            infected_data.append(state[i])
    return (infected_data,[])

def population_policy(population):
    return population,[]

def aggregate_data(state,results):
    susceptible_data = []
    infected_data = []
    recovered_data = []
    deaths_data = []
    for i in range(len(state)):
        if i%4 == 0:
            susceptible_data.append(state[i])
        if i%4 == 1:
            infected_data.append(state[i])
        if i%4 == 2:
            recovered_data.append(state[i])
        if i%4 == 3:
            deaths_data.append(state[i])
    results["susceptible"].append(sum(susceptible_data))
    results["infected"].append(sum(infected_data))
    results["recovered"].append(sum(recovered_data))
    results["deaths"].append(sum(deaths_data))

def infected_policy_reward(env):
    obs = env.reset()
    dones = False
    total_reward = 0
    results = dict()
    results["susceptible"] = []
    results["infected"] = []
    results["recovered"] = []
    results["deaths"] = [] 
    while not dones:
        aggregate_data(obs,results)
        action, _states = infected_policy(obs)
        obs, reward, dones, info = env.step(action)
        total_reward += reward
    return total_reward,results

def population_policy_reward(env):
    obs = env.reset()
    dones = False
    reward = 0
    results = dict()
    results["susceptible"] = []
    results["infected"] = []
    results["recovered"] = []
    results["deaths"] = [] 
    while not dones:
        aggregate_data(obs,results)
        action, _states = population_policy(env.total_populations)
        obs, rewards, dones, info = env.step(action)
        reward += rewards
    return reward,results

def learned_policy_reward(env,model_path):
    model = PPO2.load(model_path)
    obs = env.reset()
    dones = False
    reward = 0
    results = dict()
    actions = []
    results["susceptible"] = []
    results["infected"] = []
    results["recovered"] = []
    results["deaths"] = [] 
    while not dones:
        aggregate_data(obs,results)
        action, _states = model.predict(obs)
        actions.append((env.vaccines_per_day*(action/sum(action))).astype(int))
        print(actions[-1])
        obs, rewards, dones, info = env.step(action)
        reward += rewards
    return reward,results,actions

def no_vaccine_policy_reward(env):
    obs = env.reset()
    dones = False
    reward = 0
    results = dict()
    results["susceptible"] = []
    results["infected"] = []
    results["recovered"] = []
    results["deaths"] = [] 
    while not dones:
        aggregate_data(obs,results)
        action, _states = [0]*env.num_places,[]
        obs, rewards, dones, info = env.step(action)
        reward += rewards
    return reward,results

def rewards_from_policy(env,model_path): #Just call this
    policy_results = {}
    infected_reward,data_1 = infected_policy_reward(env)
    population_reward,data_2 = population_policy_reward(env)
    learned_reward,data_3,learned_policy_actions = learned_policy_reward(env,model_path)
    no_vaccine_reward,data_4 = no_vaccine_policy_reward(env)
    policy_results["policy_comparison"] = [infected_reward, population_reward,learned_reward,no_vaccine_reward]
    #policy_results["infected_ratio"] = data_1
    #policy_results["population_ratio"] = data_2
    policy_results["learned_policy"] = data_3
    #policy_results["no_vaccine"] = data_4
    policy_results["learned_policy_actions"] = np.asarray(learned_policy_actions)
    policy_results["place_names"] = env.place_names
    policy_results["policy_names"] = ["Infected Ratio Policy", "Population Ratio Policy", "Learned Policy", "No Policy"]
    return policy_results

def visualize_results(policy_results):
    time = np.linspace(0,len(policy_results["infected_ratio"]["infected"]),len(policy_results["infected_ratio"]["infected"]))
    fig = plt.figure()
    plt.subplot(2,2,1)
    plt.ylabel("Infected")
    plt.plot(time,policy_results["infected_ratio"]["infected"])
    plt.plot(time,policy_results["population_ratio"]["infected"])
    plt.plot(time,policy_results["learned_policy"]["infected"])
    plt.plot(time,policy_results["no_vaccine"]["infected"])

    plt.subplot(2,2,2)
    plt.ylabel("Deaths")
    plt.plot(time,policy_results["infected_ratio"]["deaths"])
    plt.plot(time,policy_results["population_ratio"]["deaths"])
    plt.plot(time,policy_results["learned_policy"]["deaths"])
    plt.plot(time,policy_results["no_vaccine"]["deaths"])

    plt.subplot(2,2,3)
    plt.ylabel("Succeptible")
    plt.plot(time,policy_results["infected_ratio"]["susceptible"])
    plt.plot(time,policy_results["population_ratio"]["susceptible"])
    plt.plot(time,policy_results["learned_policy"]["susceptible"])
    plt.plot(time,policy_results["no_vaccine"]["susceptible"])

    plt.subplot(2,2,4)
    plt.ylabel("Recovered")
    plt.plot(time,policy_results["infected_ratio"]["recovered"])
    plt.plot(time,policy_results["population_ratio"]["recovered"])
    plt.plot(time,policy_results["learned_policy"]["recovered"])
    plt.plot(time,policy_results["no_vaccine"]["recovered"])
    plt.show()

if __name__ == "__main__": #Just testing to see if it works, this won't run otherwise
    place_names,params,total_populations,initial_states = clean_data(np.load("/home/steelshot/nwHacksVaccDistr/user_data/6/fitted_model.npy",allow_pickle=True))
    env = CustomEnv(params,initial_states,total_populations,100000,30,place_names,0.95)
    policy_results = rewards_from_policy(env,180,0.95,"/home/steelshot/nwHacksVaccDistr/user_data/6/best_model")
    print(policy_results["policy_comparision"]) #Just call this
    visualize_results(policy_results)