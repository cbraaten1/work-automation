# import os
import schedule
import time

def test():
    print('Hello World')
    return schedule.CancelJob

def test2():
    print('This might work!')
    return schedule.CancelJob

def test3():
    print('This is the 3rd test!')
    return schedule.CancelJob

schedule.every(1).seconds.do(test)
schedule.every(1).minute.do(test2)
schedule.every(65).seconds.do(test3)

while 1:
    n = schedule.idle_seconds()

    if n is None:
        # no more jobs
        break
    elif n > 0:
        # sleep exactly the right amount of time.
        time.sleep(n)
    schedule.run_pending()

# Internet Documentation:
#   https://www.geeksforgeeks.org/python-script-that-is-executed-every-5-minutes/ - Original idea on how to execute code on a timer; see module #2.
#   https://schedule.readthedocs.io/en/stable/examples.html - The while loop is pulling from "Time Until Next Execution".
