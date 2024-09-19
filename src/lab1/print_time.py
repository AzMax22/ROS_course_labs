#!/usr/bin/env python3
import datetime
import time

def print_time():
    while (1):
        print(datetime.datetime.now())
        time.sleep(5)



if __name__=="__main__":
    print_time()