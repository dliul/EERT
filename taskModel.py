

class task:
    def __init__(self, C, P):
        self.wcet = 0
        self.period = 0
        self.deadline = 0
        self.criticality = 0
        self.utilization = self.wcet / self.period
        
    def get_WCET(self):
        return self.wcet
    
    def get_Period(self):
        return self.period
    
    def get_Deadline(self):
        return self.deadline
    
    def get_utilization(self):
        return self.utilization
    
    
    