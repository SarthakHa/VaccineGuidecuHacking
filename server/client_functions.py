import urllib.request

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
        print(html)
    return html

def check_existence(file_name):
    string = "http://128.2.178.158:4208/user_data/"+file_name
    try:
        with urllib.request.urlopen(string) as f:
                data = f.read().decode('utf-8')
                return data
    except:
        return False

