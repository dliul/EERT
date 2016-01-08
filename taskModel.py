

class task:
    def __init__(self, id, C, P):
        self.id = id
        self.wcet = C
        self.period = P
        self.deadline = P
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
    
    def print_task(self):
        """
        Jan-8-2016: only print out id, wcet and period
        """
        return "id: %s WCET: %s Period: %s" %(self.id, self.wcet, self.period)
    