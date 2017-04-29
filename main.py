from fitbitApiCalls import *

# functional test code
#returnJsonString = parseCurrentHR(some_url)
# returnJsonString = parseCurrentHR(test_url)
# print returnJsonString
#idea - progress bar for calories burned in a day vs calories eaten in a day or some variation


# switch_pretty_print()

print 'Most recent Heart rate recorded ' + str(current_HR()[0]) + ' at time ' + str(current_HR()[1])
