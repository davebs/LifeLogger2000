"""
Life logger -- Log window titles and time spent in each window to a CSV file.
for            CSV is visualized separately. Conveniently catches tab titles
Windows        in chrome so it works for both native software and for figuring out
               which specific sites you spend too much time on every day. 
               MIT license. author: @_davesullivan
"""

import win32gui
import time
import datetime

w = win32gui
logfile = open('logfile.csv', 'ab')

last_window_title = None
seconds_spent = 1
times_run = 0

while True:
    current_window_title = w.GetWindowText(w.GetForegroundWindow())
    time_str = datetime.datetime.now().strftime('%m-%d-%y %a %I:%M:%S')
    if current_window_title != last_window_title:
        logfile.write( '%s, %s, %i\n' % (time_str, current_window_title, seconds_spent) )
        print last_window_title
        print 'seconds spent %i' % seconds_spent
        last_window_title = current_window_title
        seconds_spent = 1
    else:
        seconds_spent += 2
    if times_run % 10 == 0:
        print 'has run for %i iterations' % times_run
    times_run += 1
    time.sleep(2)
logfile.close()
