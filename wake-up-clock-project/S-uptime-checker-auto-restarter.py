import h_clocklib as clocklib
import time as time
import _thread as thread
import os as os

#checks every 10 seconds to see if <S-listener.py> is still running. will restart the script if it does not indicate it is alive.

while (1):
    time.sleep(10)
    try:
        exec('lastUptimeRecorded = {}'.format(str(open('./h_data/lastuptime-listener.txt').read())))
        timeNow = clocklib.timeget.localtime()
        if (clocklib.comparetime.isGreaterThan(lastUptimeRecorded, timeNow)):
            print ('Spawning new process')
            thread.start_new_thread(os.system, (('{} S-listener.py'.format(str(open('./h_data/config.txt').read()).split('\n')[3].split(':')[1])),))
    except IOError as err:
        print (err)