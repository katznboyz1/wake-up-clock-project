from .timeget import *
def findDifference(time1, time2):
    DIFFERENCE = {'hours':None, 'minutes':None, 'seconds':None, 'days':None, 'months':None, 'years':None}
    return DIFFERENCE
def isGreaterThan(time1, time2): #for finding if the distance between two time dicts is positive - uses dict format in <h_clocklib.timeget.localtime()>
    ISGRTHN = False
    if (int(time2['year']) > int(time1['year'])):
        ISGRTHN = True
    elif (int(time2['month']) > int(time1['month'])):
        ISGRTHN = True
    elif (int(time2['day']) > int(time1['day'])):
        ISGRTHN = True
    elif (int(time2['hour_24HR']) > int(time1['hour_24HR'])):
        ISGRTHN = True
    elif (int(time2['minute']) > int(time1['minute'])):
        ISGRTHN = True
    elif (int(time2['second']) > int(time1['second'])):
        ISGRTHN = True
    return ISGRTHN