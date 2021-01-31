import gym
from gym import spaces
import numpy as np
from stable_baselines.common.env_checker import check_env
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common import make_vec_env
from stable_baselines import PPO2

from model import PlaceModel


class CustomEnv(gym.Env):
    def __init__(self,params,initial_states,total_populations,vaccines_per_day,max_steps,place_names,vaccine_efficacy):
        super(CustomEnv, self).__init__()
        self.num_places = params.shape[0]
        self.state_size_place = len(initial_states)//self.num_places
        self.places = []
        self.initial_states = initial_states
        
        self.params = params
        self.max_steps = max_steps
        self.time = 0
        for i in range(self.num_places):
            self.places += [PlaceModel(self.initial_states[i*self.state_size_place:(i+1)*self.state_size_place],self.params[i],total_populations[i],self.vaccine_efficacy)]

        self.action_space = spaces.Box(np.array([0.0]*self.num_places), np.array([1.0]*self.num_places),dtype=np.float32)
        self.observation_space = spaces.Box(low=0.0, high=100000000.0,shape=(len(self.initial_states),), dtype=np.float32)


    def reset(self):
        self.__init__(self.params,self.initial_states,self.total_populations,self.vaccines_per_day,self.max_steps,self.place_names,self.vaccine_efficacy)
        return self.initial_states

    def step(self,action):
        if sum(action) != 0:
            action = action/sum(action)
        total_reward = 0
        if self.time > self.max_steps:
            return self.current_state(),total_reward,True,dict()
        return self.current_state(),total_reward,False,dict()

    def render(self):
        for place in self.places:
            print(place.state)

    def current_state(self):
        state = []
        for i in range(self.num_places):
            state.append(self.places[i].state[:-1])
        return (np.array(state)).flatten()

    def close(self):
        print("bye")

