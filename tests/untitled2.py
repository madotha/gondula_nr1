# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:49:20 2018

@author: Stef
"""
#!/usr/bin/python3

import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   print("do some other stuff")
except:
   print ("Error: unable to start thread")

while 1:
   pass