# start: start time in 12-hour clock format (ending in AM or PM)
# duration: duration time that indicate the number of hours and minutes
# optional (starting day of the week) 
# the function adds the duration to the start time and return the result
# if the result is the next day the function display (next_day)
# if the result is more than one day the function display (n_days_later) where n is the number of days
# if the optional parameter is given the function display the name of the day of the week related to the result
# the name of the day of the week is displayed after the time and before the number of days later.
def add_time(start, duration, starting_week_day=False):    
    pass
    #return new_time
    
    
    
def check_time(time):
    pass

# check if the duration format is valid
def check_duration(duration):
    hours_minutes = duration.split(":")
    if len(hours_minutes) == 2 :
        if hours_minutes[0].strip().isdigit() and hours_minutes[1].strip().isdigit():
            if hours_minutes[1] not in range(1, 60):
                return [False, "Error: Invalid duration minutes."]
            else:
                return [True, [int(hours_minutes[0].strip()), int(hours_minutes[1].strip())]]
        else:
            return [False, "Error: duration hours and minutes must be digits only."]
    else:
        return [False, "Error: Invalid duration, duration must be in format (hh:mm)."]


# check if the day name is valid
def check_day_name(day_name):
    week_days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    if day_name.lower() not in week_days:
        return [False, "Error: invalid day name."]
    else:
        return [True, day_name]