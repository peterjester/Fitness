from fitbitApiCalls import *


def display():
    while(1):
        display_HR()
        time.sleep(10)
        display_weight()
        time.sleep(10)


def display_HR():
    heart_rate = current_HR()
    print "Most recent heartrate " + str(heart_rate[0]) + " at time " + str(heart_rate[1])

def display_weight():
    print "Current weight: " + str(current_weight()) + " pounds"