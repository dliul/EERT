#!/usr/bin/python
import random

class task:
    def __init__(self, id, C, P, D=0):
        self.id = id
        self.wcet = C
        self.coefficient = random.uniform(1.8, 2.3)
        self.period = P
        if D != 0:
            self.deadline = D
        else:
            self.deadline = P
        self.criticality = 0
        self.utilization = self.wcet / float(self.period)
        
    def get_WCET(self):
        return self.wcet
    
    def get_Period(self):
        return self.period
    
    def get_coefficient(self):
        return self.coefficient
    
    def get_Deadline(self):
        return self.deadline
    
    def get_utilization(self):
        return self.utilization
    
    def print_task(self):
        """
        Jan-8-2016: only print out id, wcet and period
        """
        return "id: %s WCET(PE): %s WCET(EE): %s Deadline: %s Period: %s Utilization: %s" \
                %(self.id, self.wcet, self.wcet*self.coefficient, self.deadline, self.period,self.utilization)
    