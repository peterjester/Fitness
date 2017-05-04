import datetime
from fitbitApiCalls import fitbit_request_for_url

class Activity(object):

    def __init__(self, date=datetime.datetime.now()):
        self.date = date.strftime("%Y-%m-%d")
        url = "https://api.fitbit.com/1/user/-/activities/date/" + self.date + ".json"
        self.response = fitbit_request_for_url(url)

    def refresh(self):
        url = "https://api.fitbit.com/1/user/-/activities/date/" + self.date + ".json"
        self.response = fitbit_request_for_url(url)

    '''
        @brief  - returns the number of calories output for the current day
    '''
    def calories_goal(self):
        return self.response["goals"]["caloriesOut"]

    '''
        @brief  - returns the number of calories output for the current day
    '''
    def calories_output(self):
        return self.response["summary"]["caloriesOut"]