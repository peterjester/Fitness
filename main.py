import sys
import requests
import json
import datetime

# put the token for your app in between the single quotes
token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzM0ZUUjQiLCJhdWQiOiIyMjg4U04iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd3dlaSB3c29jIHdzZXQgd2FjdCB3bG9jIiwiZXhwIjoxNDkyOTU4ODQwLCJpYXQiOjE0OTIzNTQwNDB9.fJqUblPNTX27kZ-jbRhp9sQ_LHH5q-cPA62Z3urYaB8'



'''
    @brief  - takes in request url
    @return - prettyprint formated json response as a string
    @todo   -
'''
def fitbitRequestForUrl ( url ) :
    
    print 'requesting ' + url
    response = requests.get(url, headers={'Authorization':'Bearer ' + token})
    jsonString = response.text
    
    # eval ensures our json string is not double encoded
    formatedJsonResponse = json.dumps(eval(jsonString), indent=4)
    
    return formatedJsonResponse

'''
    @brief - takes in the activities HR request url, prints the most recent HR recorded and time
    
'''
def parseCurrentHR ( url ) :
    print 'attempting to parse ' + url
    response = requests.get(url, headers={'Authorization':'Bearer ' + token})
    jsonString = json.loads(response.text)
    
    #The following block parses out the
    intradayHeartJson = jsonString["activities-heart-intraday"]
    # comes back as an array
    datasetJson = intradayHeartJson["dataset"]
    mostRecentSet = datasetJson.pop()
    latestHeartRate = mostRecentSet["value"]
    heartRateTime = mostRecentSet["time"]
    
    print 'Most recent Heart rate recorded ' + str(latestHeartRate) + ' at time ' + str(heartRateTime)


#time span for which we would like to query the API
timeNow = datetime.datetime.now() #- datetime.timedelta(minutes=30)
timeDelta = timeNow - datetime.timedelta(minutes=30)
timeStr = timeNow.strftime("%H:%M")
timeDeltaStr = timeDelta.strftime("%H:%M")

#Sample Strings
#print 'Attempting to query HR at time ' + timeDeltaStr + ' to ' + timeStr
today_heart_rate = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1sec/time/00:09/00:10.json'
test_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/time/' + timeDeltaStr + '/' + timeStr + '.json'
some_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json'
sample_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1sec/time/00:00/00:01.json'




testJsonString = parseCurrentHR(some_url)
print testJsonString


#todo - take this jsonString and parse out the most recent heart rate value
#todo - implement a subscriber to know when the heart rate is updated.
#idea - progress bar for calories burned in a day vs calories eaten in a day or some variation




