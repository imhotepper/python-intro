import requests, json


url = "https://api.punkapi.com/v2/beers" #"https://api.coinbase.com/v2/currencies"
response = requests.request("GET", url)
json_response = json.loads(response.content)          # this is traversable now
# print( json_response)
mx_ph =  float( json_response[0]["ph"])
mx_name  =  json_response[0]["name"]
mn_ph =   float( json_response[0]["ph"])
mn_name  =  json_response[0]["name"]

for  value in json_response:
        name = value["name"]
        ph = value["ph"]
        if (ph):
            if (mn_ph < float(ph)): 
                mn_name = name
                mn_ph = float(ph)
            if (mx_ph > float(ph)): 
                mx_name = name
                mx_ph = float(ph)
                
print("name = ",mx_name, " ph=", mx_ph)
print("name = ",mn_name, " ph=", mn_ph)

