import sys
import requests
import json

# put the token for your app in between the single quotes
token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzM0ZUUjQiLCJhdWQiOiIyMjg4U04iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd3dlaSB3c29jIHdzZXQgd2FjdCB3bG9jIiwiZXhwIjoxNDkyOTU4ODQwLCJpYXQiOjE0OTIzNTQwNDB9.fJqUblPNTX27kZ-jbRhp9sQ_LHH5q-cPA62Z3urYaB8'

today_heart_rate = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1sec/time/00:09/00:10.json'

url = today_heart_rate
filename = 'HR.json'

response = requests.get(url=url, headers={'Authorization':'Bearer ' + token})

jsonString = response.text

# eval ensures our json string is not double encoded
print json.dumps(eval(jsonString), indent=4)

