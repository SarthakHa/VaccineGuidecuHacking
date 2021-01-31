import numpy as np

#Modified SIRD model

class PlaceModel(object):
   
    def __init__(self,initial_state,pars,total_population,efficacy):
        self.initial_state = np.array(initial_state)
        self.state = initial_state
        self.state = np.append(self.state,0)
        self.pars = np.array(pars)
        self.timeStep = 0
        self.population = total_population
        self.efficacy = efficacy


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
