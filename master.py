import numpy as np
import sys
sys.path.append('./model_fitting')
from fitter import covsir_models
sys.path.append("./optimization")
from data_formatting import clean_data
from train_model import train_agent
from env import CustomEnv
from data_from_policy import data_from_policy
from evaluate_model import rewards_from_policy

"""
This file is used to call all our functions that we want at once. This saves the server having to call things from different places.
"""

master_path = "/home/jehand/VaccineGuidecuHacking" #editable

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
    #First getting the model fitting params
    fitting = covsir_models(countries,states)
    results = fitting.calling()
    print("Fitted data")
    print(results)
    
    #Cleaning the data
    names, pars, total_pops, i_states = clean_data(results)
    print("Cleaned Data")
    
    #Start training
    env = CustomEnv(pars,i_states,total_pops,numbvaccines,steps,names,efficacy)
    train_agent(env,0.0003,iterations,master_path+"/user_data/"+str(pathID))
    print("\n Training Complete \n")
    
    model_path = master_path+"/user_data/"+str(pathID) +"/best_model" #Defining the model path
    
    #Evaluate the model
    all_rewards = rewards_from_policy(env,numbvaccines,steps,efficacy,model_path)
    print("All Rewards Data")
    
    #Get data from policies
    data = data_from_policy(env,model_path)
    np.save(master_path+"/user_data/"+str(pathID)+"/policy_data.npy",data)
    print("Data from policy")
    
    
def run_wrapper(q):
    """
    INPUT PARAMETERS:
    ----------------
    q : dictionary
        Dictionary of all the different inputs needed
    """
    
    

if __name__ == "__main__": #Just testing to see if it works, this won't run otherwise
    run(["USA"],["Kentucky","Texas","Arizona"],180,100000,0.97,"1",iterations=10)