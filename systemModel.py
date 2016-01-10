#！/usr/bin/python


class processor:
    
    def __init__(self, id, type, a, b static, freqSet):
        self.id = id
        self.type = 
        self.alpha = a
        self.b = b
        self.static = static
        self.freqSet = freqSet
        self.currentFreq = max(freqSet)
        
    def get_alpha(self):
        return self.get_alpha
    
    def get_b(self):
        return self.get_b
    
    def get_static(self):
        return self.static
    
    def get_freqSet(self):
        return self.freqSet
    
    def get_currentFreq(self):
        return self.currentFreq
    
    
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