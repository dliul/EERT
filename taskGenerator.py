#!/usr/bin/python

import random
import sys
import argparse
import math
from taskModel import task
from scheduleAnalysis import QPA

# Using uuniFast to generate the task utilization
def uuniFast(taskNumber, totalUtil):
    sumU = totalUtil
    vectU = [];
    for i in range(1, taskNumber):
        nextSumU = float(sumU) * (random.random() ** (1 / float(taskNumber - i)))
        vectU.append(sumU - nextSumU)
        sumU = nextSumU
    vectU.append(sumU)
    if all(i <= 1 for i in vectU):
        return vectU
    else:
        return uuniFast(taskNumber, totalUtil)

""" 
To generate the task period, use the approach given by
    Paul Emberson, Roger Stafford, Robert I Davis
    "Techniques For The Synthesis Of Multiprocessor Task Sets" 
    in proceedings 1st International Workshop on Analysis Tools and Methodologies for 
    Embedded and Real-time Systems (WATERS 2010)
"""
def periodGenerator(Tmin,Tmax,Tg):
    """
    Generate period for one task from a range (Tmin, Tmax). 
    In this generation procedure, log-uniform distribution is used instead
    of uniform distribution.
    args:
        Tmin the minimum period 
        Tmax the maximum period
        Tg   the period granularity 
    Note: Tmin and Tmax must be multiples of Tg
    """
    r = random.uniform(math.log(Tmin),math.log(Tmax + Tg))
    return math.floor(math.exp(r) / Tg) * Tg
    

def main():
    taskset = []
    taskset.append(task(1,6000,31000,18000))
    taskset.append(task(2,2000,9800,9000))
    taskset.append(task(3,1000,17000,12000))
    taskset.append(task(4,90,4200,3000))
    taskset.append(task(5,8,96,78))
    taskset.append(task(6,2,12,16))
    taskset.append(task(7,10,280,120))
    taskset.append(task(8,26,660,160))
##    v = uuniFast(5, 1)
##    for i in range(len(v)):
##        T = periodGenerator(20,200,1)
##        taskset.append(task(i, int(T * v[i]), T))
        
    for i in taskset:
        print i.print_task()
    print QPA(taskset)
    
if __name__ == "__main__":
    main()