import numpy as np
import covsirphy as cs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TKAGG")

class covsir_models:
    def __init__(self,countries,states=None):
        self.countries = countries
        self.states = states
        self.n = len(states) if states>0 else len(countries)
        self.data = cs.DataLoader("model_fitting/data")
        self.jhu_data = self.data.jhu()
        self.population_data = self.data.population()
    
    #We use an SIR-D Model    
    def model(self):
        params = {} #Storing the parameter values as a dictionary ("country" : [Parameters])
        for i in range(self.n):
            if countries > 1:
                snl = cs.Scenario(self.data,self.population_data,country=self.countries[i],province=None,tau=1440)
            else:
                snl = cs.Scenario(self.data,self.population_data,countries=self.countries[0],province=self.states[i],tau=1440)
        snl.trend(show_figure=False)
        snl.estimate(cs.SIRD,timeout=60)
        if countries > 1:
            params[self.countries[i]] = pars
        else:
            params[self.states[i]] = [pars]
        return params
        
    def retrieve_population(self):
        x = 0
    
    def final_state(self):
        x = 0
        
if __name__ == "__main__": #Just for testing
    x = 0
