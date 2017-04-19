import sys
import requests
import json
import datetime

# put the token for your app in between the single quotes
token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzM0ZUUjQiLCJhdWQiOiIyMjg4U04iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd3dlaSB3c29jIHdzZXQgd2FjdCB3bG9jIiwiZXhwIjoxNDkyOTU4ODQwLCJpYXQiOjE0OTIzNTQwNDB9.fJqUblPNTX27kZ-jbRhp9sQ_LHH5q-cPA62Z3urYaB8'

today_heart_rate = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1sec/time/00:09/00:10.json'

timeNow = datetime.datetime.now() #- datetime.timedelta(minutes=30)
timeMinusOne = timeNow - datetime.timedelta(minutes=30)


timeStr = timeNow.strftime("%H:%M")
timeDeltaOneStr = timeMinusOne.strftime("%H:%M")

print 'Attempting to query HR at time ' + timeDeltaOneStr + ' to time ' + timeStr

test_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/time/' + timeDeltaOneStr + '/' + timeStr + '.json'

some_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json'

sample_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1sec/time/00:00/00:01.json'

url = test_url
filename = 'HR' + timeStr + '.json'

print 'requesting ' + url

response = requests.get(url=url, headers={'Authorization':'Bearer ' + token})

jsonString = response.text

#todo - take this jsonString and parse out the most recent heart rate value
#todo - implement a subscriber to know when the heart rate is updated.
#idea - progress bar for calories burned in a day vs calories eaten in a day or some variation

# eval ensures our json string is not double encoded
print json.dumps(eval(jsonString), indent=4)


