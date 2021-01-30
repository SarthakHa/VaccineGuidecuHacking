import numpy as np
import covsirphy as cs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TKAGG")

class covsir_models:
    def __init__(self,countries,states=None):
        self.countries = countries
        self.states = states
        self.n = len(countries) if len(countries)>1 else len(states)
        self.data = cs.DataLoader("model_fitting/data")
        self.jhu_data = self.data.jhu()
        self.population_data = self.data.population()
    
    #We use an SIR-D Model    
    def model(self):
        params = {} #Storing the parameter values as a dictionary ("country" : [Parameters])
        for i in range(self.n):
            if len(self.countries) > 1:
                snl = cs.Scenario(self.jhu_data,self.population_data,country=self.countries[i],province=None,tau=1440)
            else:
                snl = cs.Scenario(self.jhu_data,self.population_data,countries=self.countries[0],province=self.states[i],tau=1440)
            snl.trend(show_figure=False)
            snl.estimate(cs.SIRD,timeout=60)
            pars = [snl.get("rho","last"),snl.get("sigma","last"), snl.get("kappa","last")]
            if len(self.countries) > 1:
                params[self.countries[i]] = pars
            else:
                params[self.states[i]] = [pars]
        return params
        
    def retrieve_population(self):
        self.population = {} #Writing as a dictionary
        for i in range(self.n):
            if len(self.countries) > 1:
                self.population[self.countries[i]] = self.population_data.value(self.countries[i], province = None)
            else:
                self.population[self.states[i]] = self.population_data.value(self.countries[0], province = self.states[i])
        return self.population
    
    def final_state(self):
        state = {} #Writing as a dictionary
        for i in range(self.n):
            if len(self.countries) > 1:
                state[self.countries[i]] = self.jhu_data.records(self.countries[i])
            else: 
                state[self.countries[i]] = self.jhu_data.records(self.countries[0],self.states[i])
        return state
        
if __name__ == "__main__": #Just for testing
    test = covsir_models(["United States", "Canada", "United Kingdom", "Germany", "Japan"],None)#["Kentucky", "Texas", "Arizona", "Michigan", "Colorado"])
    results = test.model()
    #pop = test.retrieve_population()
    #final_state = test.final_state
    print(results)
