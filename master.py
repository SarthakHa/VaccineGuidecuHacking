import numpy as np
from fitter import covsir_models
from data_formatting import clean_data
from train_model import train_agent
from env import CustomEnv

master_path = ""

"""
This file is used to call all our functions that we want at once. This saves the server having to call things from different places.
"""

def run(countries,states,steps,numbvaccines,efficacy,pathID,iterations=100):
    """
    INPUT PARAMETERS:
    ----------------
    countries : array-like
        The countries that the user is interested in.

    states : array-like (or None)
        The states/provinces that the user would like to consider if they are keeping the country fixed. Default is None.
        
    steps : int
        The number of days that the user wants to run the simulation.
        
    numbvaccines : int
        The number of vaccines that the user wants to allocate per day.
        
    efficacy : float
        The percentage effectiveness of the vaccine that they have chosen
        
    pathID : str
        The ID of the path for the user
        
    iterations : int (default to 100)
        The number of iterations for the training to run
    """

def run_wrapper(q):
    """
    INPUT PARAMETERS:
    ----------------
    q : dictionary
        Dictionary of all the different inputs needed
    """

if __name__ == "__main__": #Just testing to see if it works, this won't run otherwise
    run(["USA"],["Kentucky","Texas","Arizona"],180,100000,0.97,"1",iterations=10)