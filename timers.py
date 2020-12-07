#Timers
#Execute code at timed intervals
#This is the first step in learning threading

#Imports and display

import time
from threading import Timer

def display(msg):
    #htt://docs.python.org/library/time.html
    print(msg + ' ' + time.strftime('%H:%M:%S'))


#Basic timer
def run_once():
    display('Run once:')
    t = Timer(5, display, ['Timeout: '])
    t.start()

run_once()
#Notice this run immediatly!
#But it also only runs once
print('Waiting.........')


#Interval timer
#Wrap it into a class
#Make it run until we stop it
#Notice we can have multiple timers at once
#https://docs.python.org/3/library/threding.html#treading.Thread.run

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
        print('Done')


#Really we are making a thread and controlling it
timer = RepeatTimer(1, display, ['Repeating'])
timer.start() #going to call run

print('threading started')
time.sleep(10) #suspends execution for the given number of seconds
print('threading finishing')

timer.cancel()
