#!/usr/bin/python

from taskModel import task

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
        
    def get_id(self):
        return self.id
    
    def get_type(self):
        return self.type
    
    def get_alpha(self):
        return self.alpha
    
    def get_b(self):
        return self.b
    
    def get_static(self):
        return self.static
    
    def get_freqSet(self):
        return self.freqSet
    
    def get_currentFreq(self):
        return self.currentFreq
    
    def get_alltasks(self):
        return self.mappedTasks
    
    def map_one_task(self,t):
        assert isinstance(t,task) == True, "mapped object is %s, not a task type " %type(t)
        self.mappedTasks.append(t)
    
    def printout_tasks(self):
        return " \n".join([i.print_task() for i in self.get_alltasks()])
    
    def printout_proc(self):
        return "id: %s type: %s a: %s b: %s static: %s" %(self.get_id(), self.get_type(), 
                                            self.get_alpha(), self.get_b(), self.get_static())
    
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
        
    def get_allProcessors(self):
        return self.allProcessors
    
    
    
def main():
    """
        For test
    """
    proc_test = processor(1,"ARM Cortex A15",3.0e-9,2.261,0.5,[1000,2000,3000])
    proc_test.map_one_task(task(1,6000,31000,18000))
    proc_test.map_one_task(task(2,2000,9800,9000))
    print proc_test.printout_tasks()
    print proc_test.printout_proc()
    
if __name__ == "__main__":
    main()