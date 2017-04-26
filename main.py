import sys
import requests
import json
import datetime

from tokens import token
from fitbitApiCalls import *

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
    
    return 'Most recent Heart rate recorded ' + str(latestHeartRate) + ' at time ' + str(heartRateTime)


#time span for which we would like to query the API
timeNow = datetime.datetime.now() #- datetime.timedelta(minutes=30)
timeDelta = timeNow - datetime.timedelta(minutes=300)
timeStr = timeNow.strftime("%H:%M")
timeDeltaStr = timeDelta.strftime("%H:%M")

#Sample Strings
#print 'Attempting to query HR at time ' + timeDeltaStr + ' to ' + timeStr
today_heart_rate = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1sec/time/00:09/00:10.json'
test_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/time/' + timeDeltaStr + '/' + timeStr + '.json'
some_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json'
sample_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1sec/time/00:00/00:01.json'



# functional test code
#returnJsonString = parseCurrentHR(some_url)
returnJsonString = parseCurrentHR(test_url)
print returnJsonString

activityForDate()

#idea - progress bar for calories burned in a day vs calories eaten in a day or some variation




