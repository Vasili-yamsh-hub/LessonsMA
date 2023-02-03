import requests as re

def get_wether(cty):
    cityid = 0
    url_1 = "http://api.openweathermap.org/data/2.5/find"
    url_2 = "http://api.openweathermap.org/data/2.5/weather"
    city = cty
    params = {
        'q'    :city,
        "type" : "like",
        "lang" :"ru",
        "appid": "8916ec839b0656f623079874ddb1afce",
        "units": "metric"   
        }  

    try: 
        res = re.get(url_1, params)  
        data = res.json()
            
        cities = ["{} ({})".format(d['name'], d['sys']['country']) for d in data['list']]
        #print("city:", cities)
        cityid = data['list'][0]["id"]
        #print("cityid = ", cityid)
        
        params_2 = {
            'id'    :cityid,
            "lang" :"ru",
            "appid": "8916ec839b0656f623079874ddb1afce",
            "units": "metric"   
            }  
            
        res2 = re.get(url_2, params_2)
        data2 = res2.json()
        #print(cityid)
        #print(data2)    
        # print("conditions:", data2['weather'][0]['description'])
        # print("temp:", data2['main']['temp'])
        # print("temp_min:", data2['main']['temp_min'])
        # print("temp_max:", data2['main']['temp_max'])
        wet = data2['weather'][0]['description']
        return wet
        
    except:
        pass
    

