import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TKAGG")

"""
This file is not called anywhere else. This is just used to plot our results when provided with a .npy file of the format 
{'policy_comparision', 'infected_ratio', 'population_ratio', 'learned_policy', 'no_vaccine', 'learned_policy_actions'}.
"""

def policy_compare_plot():
    p_data = np.abs(data["policy_comparison"])
    policies = data["policy_names"]
    fig = plt.figure()
    plt.bar(policies,p_data)
    plt.xlabel("Loss")
    plt.ylabel("Countries")
    plt.show()
    
def SIRD_plot(policy):
    SIRD_data = data[policy]
    days_arr = np.arange(1,len(SIRD_data["susceptible"])+1)
        
    fig = plt.figure(figsize=(8,8))
    fig.suptitle(policy,fontsize=20)
    i = 1
    for label in SIRD_data.keys():
        plt.subplot(2,2,i)
        plt.xlabel("Days")
        plt.ylabel(label)
        plt.plot(days_arr, SIRD_data[label])
        i+=1
    plt.show()
    
def vacc_distribution_plot():
    vacc_data = np.asarray(data["learned_policy_actions"])
    days = np.arange(1,len(vacc_data)+1)
    
    plt.figure(figsize=(8,6))
    plt.title("Vaccine Distribution per day")
    plt.xlabel("Days")
    plt.ylabel("Vaccine Distribution Per Country")
    for i in range(len(country_names)):
        plt.plot(days,vacc_data[:,i],label=country_names[i])
    plt.legend()
    plt.show()
        
if __name__ == "__main__": #Just in case it gets called even though it shouldn't
    data = np.load("model_fitting/test_data/policy_data.npy", allow_pickle=True).item()
    country_names = ["1", "2", "3", "4"]

    print(data)

    #policy_compare_plot()
    #SIRD_plot("learned_policy")
    #vacc_distribution_plot()