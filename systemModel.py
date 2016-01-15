#!/usr/bin/python

from taskModel import task
import taskGenerator as TG
import binPacking as bp

class processor:
    
    def __init__(self, id, type, a, b, static, freqSet):
        self.id = id
        self.type = type
        self.alpha = a
        self.b = b
        self.static = static
        self.freqSet = freqSet
        self.currentFreq = max(freqSet)
        self.mappedTasks = []
        self.util = 0
        # flag to indicate whether the processor already has split task
        self.split_1 = False
        self.split_2 = False
        
    def get_id(self):
        return self.id
    
    def get_type(self):
        return self.type
    
    def get_alpha(self):
        return self.alpha
    
    def get_b(self):
        return self.b
    
    def reset_map(self):
        self.mappedTasks = []
        self.util = 0
        
    def get_static(self):
        return self.static
    
    def set_split_1(self):
        self.split_1 = True
        
    def get_split_1(self):
        return self.split_1

    def set_split_2(self):
        self.split_2 = True
        
    def get_split_2(self):
        return self.split_2
        
    def get_freqSet(self):
        return self.freqSet
    
    def get_currentFreq(self):
        return self.currentFreq
    
    def get_alltasks(self):
        return self.mappedTasks
    
    def get_totalUtil(self):
        return self.util
    
    def remove_task(self,task):
        self.get_alltasks().remove(task)
        self.util -= task.get_utilization()
        
    def map_one_task(self,t):
        assert isinstance(t,task) == True, "mapped object is %s, not a task type " %type(t)
        self.mappedTasks.append(t)
        self.util += t.get_utilization()
    
    def printout_tasks(self):
        return " \n".join([i.print_task() for i in self.get_alltasks()])
    
    def printout_proc(self):
        return "id: %s type: %s a: %s b: %s static: %s utilization: %s" %(self.get_id(), self.get_type(), 
                                            self.get_alpha(), self.get_b(), self.get_static(), self.get_totalUtil())
    
class cluster:
    
    def __init__(self, id, type, num):
        self.id = id
        self.clusterType = type        
        self.numProcessor = num
        self.allProcessors = []
        
    def get_id(self):
        return self.id
    
    def get_clusterType(self):
        return self.clusterType
    
    def get_numProcessor(self):
        return self.numProcessor
    
    def init_processor(self, processor):
        self.processors.append(processor)
    
    def reset_map(self):
        for i in self.get_allProcessors():
            i.reset_map()
            
    def get_allProcessors(self):
        return self.allProcessors
    
    def add_processor(self, proc):
        assert isinstance(proc,processor) == True, 'the added object is %s, not a processor type' \
                                            %type(proc)
        self.allProcessors.append(proc)
    
    def printout_cluster(self):
        return "id: %s type: %s number of processors: %s" %(self.get_id(), self.get_clusterType(), 
                                                            self.get_numProcessor())
    
def main():
    """
        For test
    """
    cl = cluster(1, "ARM Cortex A15", 3)
    freqBig = [800,1000,1200,1400,1600,1800,2000]
    cl.add_processor(processor(1,"ARM Cortex A15",3.0e-9,2.261,0.5,freqBig))
    cl.add_processor(processor(2,"ARM Cortex A15",3.0e-9,2.261,0.5,freqBig))
    cl.add_processor(processor(3,"ARM Cortex A15",3.0e-9,2.261,0.5,freqBig))
    taskset = TG.generateTasks(6, 2)
    
    print cl.printout_cluster()
    for i in taskset:
        print i.print_task()
    print "total utilization: %s" %(sum([i.get_utilization() for i in taskset]))
    fd = bp.FFD(taskset, cl)
    print "==================================================================="
    print "==================================================================="
    print "FFD"
    for i in fd.get_allProcessors():
        print "processor %s" %i.get_id()
        print i.printout_proc()
        print i.printout_tasks()
    bd = bp.FFD_split(taskset, cl)
    print "==================================================================="
    print "==================================================================="
    print "FFD with split"
    for i in bd.get_allProcessors():
        print "processor %s" %i.get_id()
        print i.printout_proc()
        print i.printout_tasks()
    #proc_test.map_one_task(task(1,6000,31000,18000))
    #proc_test.map_one_task(task(2,2000,9800,9000))
    #print proc_test.printout_tasks()
    #print proc_test.printout_proc()
    #print proc_test.get_totalUtil()
    
if __name__ == "__main__":
    main()