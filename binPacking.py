#!/usr/bin/python
from taskModel import task
import math
import scheduleAnalysis as sa

def FFD(taskset, clusters):
    tasks = sorted(taskset, key=lambda x:x.utilization, reverse=True)
    clusters.reset_map()
    for t in tasks:
        for p in clusters.get_allProcessors():
            if p.get_totalUtil() + t.get_utilization() <= 1:
                p.map_one_task(t)
                break
    
    return clusters

def WFD(taskset, clusters):
    tasks = sorted(taskset, key=lambda x:x.utilization, reverse=True)
    clusters.reset_map()
    for t in tasks:
        for p in sorted(clusters.get_allProcessors(), key=lambda x: x.get_totalUtil(), reverse=False):
            #print p.get_totalUtil()
            if p.get_totalUtil() + t.get_utilization() <= 1:
                p.map_one_task(t)
                break
    
    return clusters

def FFD_split(taskset, clusters):
    tasks = sorted(taskset, key=lambda x:x.utilization, reverse=True)
    clusters.reset_map()
    for t in tasks:
        for p in clusters.get_allProcessors():
            if p.get_totalUtil() + t.get_utilization() <= 1:
                p.map_one_task(t)
                break
            else:
                """
                    1. Set the total Utilization = 1, then compute the corresponding wcet for the first
                    part of split task. Derive the respective parameters according to the paper
                """
                mappedTasks = p.get_alltasks()
                leftCapacity = 0.999 - p.get_totalUtil()
                wcet_1 = leftCapacity * t.get_period()
                # Once wcet_1 is not equal to 0, the algorithm tries to reduce wcet
                while wcet_1 != 0:
                    spt_1 = task("%s-1" %t.get_id(), wcet_1, t.get_period(), wcet_1)
                    # Check the total utilization less than 1
                    if p.get_totalUtil() + spt_1.get_utilization() <= 1:                            
                        mappedTasks.append(spt_1)
                        # Use QPA to test the schedulability of the new mapping
                        # variable result is to store the result
                        # if schedulable, it's equal to -1
                        # if unschedulable, it's equal to the time instance failing QPA
                        result = sa.QPA(mappedTasks)
                        if  result == -1:
                            p.map_one_task(spt_1)
                            wcet_2 = t.get_wcet() - wcet_1
                            spt_2 = task(t.get_id() + "-2", wcet_2, t.get_period(), wcet_2)
                            for n in clusters.get_allProcessors():
                                if n.get_totalUtil() + spt_2.get_utilization() <= 1 \
                                and n.get_split() == False:
                                    mapTasks_2 = n.get_alltasks()
                                    mapTasks_2.append(spt_2)
                                    if sa.QPA(mapTasks_2) == -1:
                                        n.map_one_task(spt_2)
                                        break
                            break
                        else:
                            # can not pass the QPA test
                            oth = sum([(math.ceil((result + i.get_period()
                                        - i.get_deadline)/i.get_period())) * i.get_wcet
                                         for i in mappedTasks if i == spt_1])
                                        
    return clusters

def compute_new_wcet(db, task, t):
    deadline = task.get_deadline()
    while deadline != 0:
        nextDeadline = (t - db) / math.ceil((t + task.get_period() - deadline - 1)/task.get_period())
        if deadline == nextdeadline:
            return deadline
        else:
            deadline = nextDeadline
            
def main():
    proc_test = processor(1,"ARM Cortex A15",3.0e-9,2.261,0.5,[1000,2000,3000])
    proc_test.map_one_task(task(1,6000,31000,18000))
    proc_test.map_one_task(task(2,2000,9800,9000))

if __name__ == "__main__":
    main()