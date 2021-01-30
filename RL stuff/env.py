import gym
from gym import spaces
import numpy as np
from stable_baselines.common.env_checker import check_env
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common import make_vec_env
from stable_baselines import PPO2

from model import PlaceModel


class CustomEnv(gym.Env):
    def __init__(self,params,initial_states,total_populations,vaccines_per_day):
        super(CustomEnv, self).__init__()
        self.num_places = params.shape[0]
        self.state_size_place = len(initial_states)//self.num_places
        self.places = []
        self.initial_states = initial_states
        self.vaccines_per_day = vaccines_per_day
        self.total_populations = total_populations
        self.params = params
        self.time = 0
        for i in range(self.num_places):
            self.places += [PlaceModel(self.initial_states[i*3:i*3+self.state_size_place],self.params[i],total_populations[i])]
        self.action_space = spaces.Box(np.array([0.0]*self.num_places), np.array([1.0]*self.num_places),dtype=np.float32)
        self.observation_space = spaces.Box(low=0.0, high=100000000.0,shape=(len(self.initial_states),), dtype=np.float32)


    def reset(self):
        self.__init__(self.params,self.initial_states,self.total_populations,self.vaccines_per_day)
        return self.initial_states

    def step(self,action):
        if sum(action) != 0:
            action = action/sum(action)
        total_reward = 0
        for i in range(self.num_places):
            state,reward = self.places[i].step(action[i]*self.vaccines_per_day)
            total_reward += reward
        self.time += 1
        if self.time > 180:
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

initial_states = np.array([6185501.0,177589.0,360087.0,8823.0,6435833.0,254866.0,38445.0,2856.0,6028735.0,172488.0,513383.0,17394.0])
total_populations = np.array([673200,4500000,12700000])
params = np.array([[0,0.0369,0.0228,0.000387],[0.002158,0.03058,0.002921,0.0002043],[0.0,0.029299,0.01911,0.000444]])


env = CustomEnv(params,initial_states,total_populations,200000)
check_env(env)

model = PPO2(MlpPolicy, env, verbose=1,tensorboard_log="./tty/",gamma=1.0,n_steps=20)
model.learn(total_timesteps=800000)
model.save("ppo2_cartpole")



# It will check your custom environment and output additional warnings if needed
obs = env.reset()
for i in range(200):
    obs, rewards, dones, info = env.step(np.array([0.5,0.3,0.2]))
    #print(rewards)

