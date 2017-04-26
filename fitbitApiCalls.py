import sys
import time
import requests
import json
import datetime

timeNow = datetime.datetime.now()


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


def activityForDate() :
    print timeNow
    time.sleep(30)
    print timeNow
    url = 'https://api.fitbit.com/1/user/[user-id]/activities/date/[date].json'

