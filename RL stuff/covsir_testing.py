import numpy as np
import covsirphy as cs
from pprint import pprint
import datetime 

#Params as 2D array
#Population as 1D array

class covsir_models:
    """
    Class to determine the best fit parameters for different countries 

    """

    def __init__(self,countries,states=None):
        self.data = cs.DataLoader("input")
        self.countries = countries
        self.states = states
        self.jhu_data = self.data.jhu()
        self.n = len(countries) if len(countries)>1 else len(states)
        self.population_data = self.data.population()
    
    def retrieve_population(self):
        self.population = []
        for i in range(self.n):
            if len(self.countries)>1:
                self.population.append(self.population_data.value(self.countries[i], province = None))
            else:
                self.population.append(self.population_data.value(self.countries[0], province = self.states[i]))
        return self.population

    #We model with a SIR-D model
    def model(self):
        params = []
        for i in range(self.n):
            if len(self.countries)>1:
                snl = cs.Scenario(self.jhu_data,self.population_data,country=self.countries[i],province=None)
            else:
                snl = cs.Scenario(self.jhu_data,self.population_data,country=self.countries[0],province=self.states[i])
            #snl.summary(columns=["Start","End",*cs.SIRD.PARAMETERS,"Rt"])
            past_date = (datetime.datetime.now()-datetime.timedelta(days=30)).strftime("%d%b%Y")
            snl.first_date = past_date
            snl.trend()
            snl.estimate(cs.SIRD)
            snl.clear(include_past=True, name="Main")

if __name__ == "__main__":
    data_loader = cs.DataLoader("input")
    jhu_data = data_loader.jhu()
    population_data = data_loader.population()
    test = covsir_models(["USA"],["Texas", "Kentucky", "Indiana"])
    test.model()