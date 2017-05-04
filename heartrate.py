from fitbitApiCalls import *

class Heartrate(obj):

    def __init__(self,date=datetime.datetime.now()):
        self.date = date.strftime("%Y-%m-%d")
        url = "https://api.fitbit.com/1/user/-/activities/date/" + self.date + ".json"
        self.response = fitbit_request_for_url(url)

    '''
        @brief  - returns the number of calories output for the current day
    '''
    def current_HR(self):
        self.response.pop()["value"], self.response.pop()["time"]