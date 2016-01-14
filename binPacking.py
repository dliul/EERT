#!/usr/bin/python

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

def main():
    proc_test = processor(1,"ARM Cortex A15",3.0e-9,2.261,0.5,[1000,2000,3000])
    proc_test.map_one_task(task(1,6000,31000,18000))
    proc_test.map_one_task(task(2,2000,9800,9000))

if __name__ == "__main__":
    main()