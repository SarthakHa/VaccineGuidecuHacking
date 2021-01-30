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
    
    #We use an SIR-D Model    
    def model(self):
        x = 0
        
    def retrieve_population(self):
        x = 0
    
    def final_state(self):
        x = 0
        
if __name__ == "__main__": #Just for testing
    x = 0