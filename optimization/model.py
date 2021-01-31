import numpy as np

#Modified SIRD model
"""
Class containing model for state variables
initial_state containts initial state variables: [S,I,R,D,V]
pars contains parameters for the model: [beta,gamma,alpha] where
beta: transmission, gamma: recovered proportion, alpha: death proportion
"""
class PlaceModel(object):
    """
    INPUT PARAMETERS:
    --------------
    initial_state : array-like
        n-dimensional array describing the state of the initial system. i.e. number of succeptible, infected etc.

    pars : array-like
        2D array for the parameter values [beta,gamma,alpha] for each country/state/province.

    total_population : array-like
        1D array of the population of each country/state/province.
    """
    def __init__(self,initial_state,pars,total_population,efficacy):
        self.initial_state = np.array(initial_state)
        self.state = initial_state
        self.state = np.append(self.state,0)
        self.pars = np.array(pars)
        self.timeStep = 0
        self.population = total_population
        self.efficacy = efficacy

    def get_susceptible(self):
        return self.state[0]

    def get_infected(self):
        return self.state[1]

    def get_recovered(self):
        return self.state[2]
    
    def get_deaths(self):
        return self.state[3]

    def get_vaccinated(self):
        return self.state[4]

    def get_current_time(self):
        return self.timeStep

    def get_params(self):
        return self.params

    def set_params(self,params):
        self.params = params

    def set_initial_state(self,initial_state):
        self.initial_state = initial_state

    def step(self,action=0):
        action = int(action*self.efficacy)
        dS = - (self.pars[0]*self.state[0]*self.state[1]/self.population) - action
        dI = -dS - action - (self.pars[1]+self.pars[2])*self.state[1]
        dR = self.pars[1]*self.state[1]
        dD = self.pars[2]*self.state[1]
        changes = [dS,dI,dR,dD,action]
       
        for i in range(len(changes)):
            self.state[i] = max(0,self.state[i]+changes[i])

        self.timeStep += 1
        return self.state,-dD

    def reset(self):
        self.__init__()

    def simulate(self,n):
        results = np.empty((3,n),dtype=np.int64) 
        for i in range(n):
            obs,reward = self.step()
            results[0][i] = obs[1]
            results[1][i] = obs[4]
            results[2][i] = obs[3]
        return results