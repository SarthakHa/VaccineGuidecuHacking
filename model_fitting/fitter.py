import numpy as np
import covsirphy as cs
import datetime

"""
Class to determine the best fit parameters for each country using covsirphy:
https://lisphilar.github.io/covid19-sir/covsirphy.html 

We assume that the user is either looking at multiple countries, or at different states/provinces
within one country of their choosing.

The function 'retrieve_population' will output the population of each country/state.

The function 'model' will output a dictionary of the best fit parameters for each of these countries according to a SIR-D 
model.
"""

class covsir_models:
    """
    INPUT PARAMETERS:
    ----------------
    countries : array-like
        The countries that the user is interested in.

    states : array-like (or None)
        The states/provinces that the user would like to consider if they are keeping the country fixed. Default is None.
    """
    def __init__(self,countries,states=None):
        self.countries = countries
        self.states = states
        self.n = len(countries) if len(countries)>1 else len(states) #Number of variable countries or states
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
            past_date = (datetime.datetime.now()-datetime.timedelta(days=40)).strftime("%d%b%Y")
            snl.first_date = past_date #Defining the first date of data to be 40 days ago.
            snl.trend(show_figure=False)
            snl.disable(phases=["0th"]) #Ignoring the first phase as we are starting the data at an arbitrary point.
            snl.estimate(cs.SIRD,timeout=60) #Setting max time to be a minute so that it does not run too long
            pars = [snl.get("rho","last"),snl.get("sigma","last"), snl.get("kappa","last")]
            if len(self.countries) > 1:
                params[self.countries[i]] = pars
            else:
                params[self.states[i]] = pars
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
                df, _ = self.jhu_data.records(self.countries[i])
                state[self.countries[i]] = df.tail(1)
            else:
                df, _ = self.jhu_data.records(self.countries[0],self.states[i])
                state[self.states[i]] = df.tail(1)
        return state
    
    def calling(self): #so that it is simpler for the other class to call and get all the data
        populations = self.retrieve_population()
        pars = self.model()
        state = self.final_state()
        return [populations, pars, state]
        
if __name__ == "__main__": #Just for testing
    test = covsir_models(["United States"],["Kentucky", "Texas", "Arizona", "Michigan", "Colorado"])#["United States", "Canada", "United Kingdom", "Germany", "Japan"]
    results = test.calling()
    print(results)