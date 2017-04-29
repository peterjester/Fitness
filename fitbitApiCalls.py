import time
import requests
import json
import datetime
import sys

from tokens import token

#todo - make fitbit class with different objects i.e. activity, food, hr, etc

'''
    @brief - global value for whether or not you would like the json strings
                return in pretty print
'''
pretty_print_global = False
def switch_pretty_print():
    global pretty_print_global
    pretty_print_global = not pretty_print_global
    return pretty_print_global

'''
    @brief  - takes in request url
    @return - json object response 
    @todo   - catch exceptions
'''
def fitbit_request_for_url(url, pretty=False):
    response = requests.get(url, headers={'Authorization': 'Bearer ' + token,
                                          'Accept-Language': 'en_US'})
    print 'requesting ' + url
    print "requests reminaing " + response.headers["Fitbit-Rate-Limit-Remaining"]
    json_response = response.json()
    if json_response["errors"]:
        reset_time = str(datetime.timedelta(seconds=int(response.headers["Fitbit-Rate-Limit-Reset"])))
        print "time limit resets " + reset_time + " seconds"
        sys.exit("Received an error")
    return json_response

'''
    @brief  - returns the current time, and the time minus the parameter 
              in minutes as a tuple. Default is 300
    @note   - to access the current time, call "time_now_time_them()[0]"
    @return - prettyprint formatted json response as a string
'''
def time_now_time_then(delta=300) :
    time_now = datetime.datetime.now()
    time_delta = time_now - datetime.timedelta(minutes=delta)
    #time span for which we would like to query the API
    time_str = time_now.strftime("%H:%M:%S")
    time_delta_str = time_delta.strftime("%H:%M:%S")
    return time_str, time_delta_str

'''
    @brief  - returns the activity json object for the given date. default is today
'''
def activity(date=datetime.datetime.now()):
    date = date.strftime("%Y-%m-%d")
    url = "https://api.fitbit.com/1/user/-/activities/date/" + date + ".json"
    return fitbit_request_for_url(url)

'''
    @brief  - returns the number of calories output for the current day
'''
def calories_output():
    return activity()["summary"]["caloriesOut"]

'''
    @brief  - returns the number of calories output for the current day
'''
def calories_goal():
    return activity()["goals"]["caloriesOut"]

'''
    @brief  - returns the weight json object for the given date. default is today
'''
def weight(date=datetime.datetime.now()):
    date = date.strftime("%Y-%m-%d")
    url = 'https://api.fitbit.com/1/user/-/body/log/weight/date/' + date + '.json'
    return fitbit_request_for_url(url)

'''
    @brief  - returns most recent weight
'''
def current_weight():
    return weight()["weight"].pop()["weight"]


'''
    @brief  - returns the number of calories output for the current day
'''
def current_HR():
    url = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1sec.json'
    data = fitbit_request_for_url(url, False)["activities-heart-intraday"]["dataset"]
    return data.pop()["value"], data.pop()["time"]
