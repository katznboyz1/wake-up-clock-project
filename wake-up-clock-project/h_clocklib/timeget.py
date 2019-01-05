from time import localtime as lt
def localtime(): #returns the details about the local time in a dict
    ENDTIMEDICT = {}
    LOCALTIME = lt()
    for partition in range(len(LOCALTIME)):
        if (partition == 0):
            ENDTIMEDICT['year'] = LOCALTIME[partition]
        elif (partition == 1):
            ENDTIMEDICT['month'] = LOCALTIME[partition]
        elif (partition == 2):
            ENDTIMEDICT['day'] = LOCALTIME[partition]
        elif (partition == 3):
            ENDTIMEDICT['hour_24HR'] = LOCALTIME[partition]
            ENDTIMEDICT['hour_12HR'] = int(LOCALTIME[partition])
            if (int(ENDTIMEDICT['hour_24HR'] > 12)):
                ENDTIMEDICT['hour_12HR'] = int(LOCALTIME[partition]) - 12
                ENDTIMEDICT['pm/am'] = 'pm'
            else:
                ENDTIMEDICT['pm/am'] = 'am'
        elif (partition == 4):
            ENDTIMEDICT['minute'] = LOCALTIME[partition]
        elif (partition == 5):
            ENDTIMEDICT['second'] = LOCALTIME[partition]
        elif (partition == 6):
            ENDTIMEDICT['weekday'] = LOCALTIME[partition]
        elif (partition == 7):
            ENDTIMEDICT['yearday'] = LOCALTIME[partition]
        elif (partition == 8):
            ENDTIMEDICT['daylightsavingtime'] = bool(int(LOCALTIME[partition]))
    return ENDTIMEDICT
def getDisplayableTime(hourFormat = '12', dayMonthFormat = 'MM/DD'): #returns a string that can be used to display the time, such as "12/34/56 - 78:90"
    TIME = localtime()
    TIMEFORMATTED = '{}:{}'.format((TIME['hour_12HR'] if hourFormat == '12' else TIME['hour_24HR']), (TIME['minute'] if len(str(TIME['minute'])) == 2 else '0' + str(TIME['minute'])))
    return TIMEFORMATTED
def getSecondsSinceMidnight(timenow = ''):
    if (timenow == ''):
        timenow = localtime()
    seconds = 0
    seconds_in_hours = timenow['hour_24HR']
    seconds_in_hours *= 3600
    seconds += seconds_in_hours
    seconds_in_minutes = timenow['minute']
    seconds_in_minutes *= 60
    seconds += seconds_in_minutes
    seconds += timenow['second']
    return seconds