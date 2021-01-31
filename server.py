import http.server
import socketserver
from threading import Thread 
from urllib.parse import urlparse
from urllib.parse import parse_qs
import time
import numpy as np
import sys,os,subprocess,socket
sys.path.append('./model_fitting')
from fitter import covsir_models
sys.path.append("./optimization")
from data_formatting import clean_data
from train_model import train_agent
from env import CustomEnv
from evaluate_model import rewards_from_policy
from data_from_policy import data_from_policy


master_path = "/home/sgirdhar/nwHacksVaccDistr"

def port_in_use(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    if result == 0:
      return True
    else:
      return False

def find_open_port():
    for i in range(6006,9000):
        if not port_in_use(i):
            return i
    return None

def train_model(pathID,model_fit,numbvaccines,steps,efficacy,iterations,open_port):
    save_path = master_path +'/user_data/'+str(pathID)
    #Cleaning the data
    names, pars, total_pops, i_states = clean_data(model_fit)
    print("Cleaned Data")
        
    #Start training
    env = CustomEnv(pars,i_states,total_pops,numbvaccines,steps,names,efficacy)
    train_agent(env,0.0001,iterations,save_path,open_port)
    print("\n Training Complete \n")

    #Evaluate the model
    policy_data = rewards_from_policy(env,save_path+"/best_model")

    print("All Rewards Data")
    np.save(save_path+"/policy_data.npy",policy_data)

class ClientThread(Thread):
    def __init__(self,pathID,model_fit,numbvaccines,steps,efficacy,iterations,open_port): 
        Thread.__init__(self) 
        self.pathID = pathID
        self.model_fit = model_fit
        self.numbvaccines = numbvaccines
        self.steps = steps
        self.efficacy = efficacy
        self.iterations = iterations
        self.open_port = open_port
    def run(self):
         train_model(self.pathID,self.model_fit,self.numbvaccines,self.steps,self.efficacy,self.iterations,self.open_port)
        


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self,data):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(data, "utf-8"))

    def do_GET(self):          
        q=parse_qs(urlparse(self.path).query)
        print(q)
        #if not os.path.exists('/home/sgirdhar/nwHacksVaccDistr/user_data/'+q['uid'][0]):
        #    os.makedirs('/home/sgirdhar/nwHacksVaccDistr/user_data/'+q['uid'][0])
        self.run_wrapper(q)
        


    def run_wrapper(self,q):
        unique_id = int(q['uid'][0])
        countries = q['countries'][0].split(',') 
        steps = int(q['total_time'][0])
        efficacy = float(q['efficacy'][0])
        states = q['states'][0].split(',')
        iterations = int(q['iterations'][0])
        numbvaccines = int(q['total_vaccines'][0])
        self.run(countries,states,steps,numbvaccines,efficacy,unique_id,iterations=iterations)

    def run(self,countries,states,steps,numbvaccines,efficacy,pathID,iterations=100,load_fit=False):
        save_path = master_path +'/user_data/'+str(pathID)
        if not os.path.exists(save_path):
                os.makedirs(save_path)
        if not load_fit:
            #First getting the model fitting params
            fitting = covsir_models(countries,states)
            results = fitting.calling()
            print("Fitted data")
            np.save(save_path+"/fitted_model.npy", results)
        
        else:
            results = np.load(save_path+"/fitted_model.npy",allow_pickle=True)
                
        #Find Port for tensorboard process
        open_port = find_open_port()
        print("Found Open Port on",open_port)
        
        self._set_headers(str(open_port))
        newThread = ClientThread(pathID,results,numbvaccines,steps,efficacy,iterations,open_port)
        newThread.start()

if __name__ == "__main__": 
    handler_object = MyHttpRequestHandler

    PORT = 6968
    my_server = socketserver.ThreadingTCPServer(("", PORT), handler_object)

    # Star the serve
    my_server.serve_forever()
