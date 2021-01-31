import numpy as np

def clean_data(data):
    initial_states = []
    place_names = np.array([])
    total_populations = np.array([])
    params = []
    for place in data[0].keys():
        place_names = np.append(place_names,place)
        total_populations = np.append(total_populations,data[0][place])
        params.append([data[1][place][0],data[1][place][1],data[1][place][2]])
        P = data[2][place]["Confirmed"]
        R = data[2][place]["Recovered"]
        F = data[2][place]["Fatal"]
        I = data[2][place]["Infected"]
        initial_states += [data[0][place]-P,I,R,F]
    return place_names,np.array(params),total_populations,np.array(initial_states).flatten()

