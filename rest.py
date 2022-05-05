import requests, json

# check this: https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/

url = "https://api.coinbase.com/v2/currencies"
response = requests.request("GET", url)
json_response = json.loads(response.text)          # this is traversable now
print( json_response)