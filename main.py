from display import display
# from fitbitApiCalls import *
import time

from activity import *

# functional test code
# idea - progress bar for calories burned in a day vs calories eaten in a day or some variation

# print current_weight()

# current_HR()

obj = Activity()

print obj.calories_goal()
obj.refresh()
print obj.calories_goal()

