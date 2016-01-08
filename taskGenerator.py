#!/usr/bin/python

import random
import sys
import argparse
import math
from taskModel import task

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
    v = uuniFast(5, 2)
    for i in range(len(v)):
        T = periodGenerator(20,200,1)
        taskset.append(task(i, int(T * v[i]), T))
        
    for i in taskset:
        print i.print_task()
    
if __name__ == "__main__":
    main()