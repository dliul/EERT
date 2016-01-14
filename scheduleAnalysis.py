#!/usr/bin/python
import math
from taskModel import task
"""
Most of theoretical foundations are from the following paper,
    Fengxiang Zhang; Burns, A., 
    "Schedulability Analysis for Real-Time Systems with EDF Scheduling," 
    in Computers, IEEE Transactions on , vol.58, no.9, pp.1250-1258, Sept. 2009
"""
def QPA(taskset):
    currTaskSet = taskset
    totalUtil = sum([i.utilization for i in currTaskSet])
    #assert totalUtil <= 1
    L = compute_bound(taskset,totalUtil)
    #print "L",L
    t = compute_dmax(L,taskset)
    #print "t",t
    dmin = min([i.deadline for i in taskset])
    ht = DBF(t,currTaskSet)
    while  ht <= t and ht >= dmin:
        print "t = %s,   h(t) = %s" %(t, ht)
        if ht < t:
            t = ht
        else:
            t = compute_dmax(t, taskset)
        ht = DBF(t,currTaskSet)
    print "t = %s,   h(t) = %s" %(t, ht)
    if ht <= dmin :
        return -1
    else:
        return t
                
         

"""
Demand bound function for a taskset
"""
def DBF(t,taskset):
    dbf = sum([max(0,1+ math.floor((t - i.deadline)/i.period))*i.wcet for i in \
                taskset])
    return dbf

"""
Compute the bound used for DBF test. 
The bound is computed using Eq. (7) from QPA papaer.
"""
def compute_bound(taskset, U):
    w0 = sum([i.wcet for i in taskset])
    LB = compute_LB(w0, taskset)
    if U == 1:
        return LB
    else:
        """
        compute la using Eq. (2)
        """
        maxDeadline = max([i.deadline for i in taskset])
        LastTerm = sum([(i.period - i.deadline)*i.utilization for i in taskset]) \
                    / (1 - U)
        return min(LB,max(maxDeadline,LastTerm))

"""
Compute lb using Eq. (5),(6)  
"""    
def compute_LB(w0, taskset):
    w1 = sum([math.ceil(w0/i.period)*i.wcet for i in taskset])
    if w1 == w0:
        return w1
    else:
        return compute_LB(w1,taskset)
    
def compute_dmax(t, taskset):
    tmp_dmax = 0
    dj = 0
    for i in taskset:
        if i.deadline < t:
            dj = math.floor((t - i.deadline) / i.period)*i.period + i.deadline
            if dj == t:
                dj = dj - i.period
            if dj > tmp_dmax:
                tmp_dmax = dj
    return tmp_dmax
        
def main():
    taskset = []
    taskset.append(task(1,2,12,16))
    print DBF(16984,taskset)
    print compute_dmax(16984,taskset)
    return 0
    
    
if __name__ == "__main__":
    main()