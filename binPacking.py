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
        print t.print_task()
        map_flag = False # use this flag to check whether the task is mapped
        for p in clusters.get_allProcessors():
            if p.get_totalUtil() + t.get_utilization() <= 1:
                p.map_one_task(t)
                if sa.QPA(p.get_alltasks()) == -1:
                    break
                p.remove_task(t)
            else:
                """
                    1. Set the total Utilization = 0.99, then compute the corresponding wcet for the first
                    part of split task. Derive the respective parameters according to the paper
                """
                # mappedTasks = p.get_alltasks()
                leftCapacity = 0.99 - p.get_totalUtil()
                wcet_1 = leftCapacity * t.get_period()
                # Once wcet_1 is not equal to 0, the algorithm tries to reduce wcet
                while wcet_1 != 0:
                    spt_1 = task("%s-1" %t.get_id(), wcet_1, t.get_period(), wcet_1,t.get_coefficient())
                    # Check the total utilization less than 1
                    # No split part 1 on the same processor
                    if p.get_totalUtil() + spt_1.get_utilization() <= 1 and not p.get_split_1():                            
                        p.map_one_task(spt_1)
                        # Use QPA to test the schedulability of the new mapping
                        # variable result is to store the result
                        # if schedulable, it equals -1
                        # if unschedulable, it equals the time instance failing QPA
                        result = sa.QPA(p.get_alltasks())
                        if  result == -1:
                            p.set_split_1()
                            # p.map_one_task(spt_1)
                            wcet_2 = t.get_wcet() - wcet_1
                            spt_2 = task("%s-2" %t.get_id(), wcet_2, t.get_period(), wcet_2)
                            for n in clusters.get_allProcessors():
                                if n.get_totalUtil() + spt_2.get_utilization() <= 1 \
                                and not spt_1 in n.get_alltasks():
                                    #mapTasks_2 = n.get_alltasks()
                                    n.map_one_task(spt_2)
                                    if sa.QPA(n.get_alltasks()) == -1:
                                        # remove the mapped task
                                        # mapTasks_2.remove(spt_2)
                                        # n.map_one_task(spt_2)
                                        map_flag = True
                                        break
                                    else:
                                        n.remove_task(spt_2)
                            break
                        else:
                            # cannot pass the QPA test
                            # c1 = (result - oth)/ math.ceil((result + i.get_period() - c1) / i.get_period()) - 1
                            oth = sum([(math.ceil((result + i.get_period() - i.get_deadline())/i.get_period())) * i.get_wcet()
                                         for i in p.get_alltasks() if i != spt_1])
                            wcet_1 = compute_new_wcet(oth, spt_1, result)
                            p.remove_task(spt_1)
                    else:
                        if p.get_split_1():
                            break
                if map_flag:
                    break # complete the mapping                    
    return clusters


def compute_new_wcet(db, task, t):
    deadline = task.get_deadline()
    while deadline != 0:
        nextDeadline = (t - db) / math.ceil((t + task.get_period() - deadline - 1)/task.get_period())
        if deadline == nextDeadline:
            return deadline
        else:
            if nextDeadline < 1:
                return 0
            deadline = nextDeadline
            
def main():
    proc_test = processor(1,"ARM Cortex A15",3.0e-9,2.261,0.5,[1000,2000,3000])
    proc_test.map_one_task(task(1,6000,31000,18000))
    proc_test.map_one_task(task(2,2000,9800,9000))

if __name__ == "__main__":
    main()