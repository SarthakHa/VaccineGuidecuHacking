import urllib.request
import numpy
import io
import time

def send_request(countries,states,total_vaccines,efficacy,total_time,iterations,uid):
    string = "http://128.2.178.158:6968?uid={0}&total_time={1}&total_vaccines={2}&efficacy={3}&iterations={4}&countries=".format(uid,total_time,total_vaccines,efficacy,iterations)
    for country in countries:
        string += country+","
    if len(countries) != 0: string = string[:-1]
    if states == []: string += "&states=None"
    else:
        string += "&states="
        for state in states:
            string += state+","
        string = string[:-1]
    print(string)
    with urllib.request.urlopen(string) as f:
        html = f.read().decode('utf-8')
    return html

def check_existence(uid,file_name):
    string = "http://128.2.178.158:4208/user_data/"+str(uid)+"/"+file_name
    try:
        with urllib.request.urlopen(string) as f:
                data = f.read()
                formatted_data = numpy.load(io.BytesIO(data),allow_pickle=True)
                
                return formatted_data
    except:
        return []

if __name__ == "__main__": #Just testing to see if it works, this won't run otherwise
    port_no = send_request(["USA"],["Kentucky","Texas","Arizona"],100000,0.97,180,100,4)
    print("link is ", "http://128.2.178.158:"+str(port_no))
    while True:
        time.sleep(5)
        temp = check_existence(4,"policy_data.npy")
        if len(temp) != 0:
            print(temp)
            break
        print("couldn't find")
