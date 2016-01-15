#!/usr/bin/python
import random

class task:
    def __init__(self, id, C, P, D=0, CE=0):
        self.id = id
        self.wcet = C
        # coefficient for the heterogeneous platform
        if CE == 0:
            self.coefficient = random.uniform(1.8, 2.3)
        else:
            self.coefficient = CE
        self.period = P
        if D != 0:
            self.deadline = D
        else:
            self.deadline = P
        self.criticality = 0
        self.utilization = self.wcet / float(self.period)
    
    def get_id(self):
        return self.id
    
    def get_wcet(self):
        return self.wcet
    
    def get_period(self):
        return self.period
    
    def get_coefficient(self):
        return self.coefficient
    
    def get_deadline(self):
        return self.deadline
    
    def get_utilization(self):
        return self.utilization
    
    def print_task_verbose(self):
        """
        Jan-8-2016: only print out id, wcet and period
        """
        return "id: %s WCET(PE): %5.2f WCET(EE): %5.2f Deadline: %5.2f Period: %5.2f Utilization: %5.2f" \
                %(self.id, self.wcet, self.wcet*self.coefficient, self.deadline, self.period,self.utilization)
    
    def print_task(self):
        return "id: %s C(PE): %5.2f C(EE): %5.2f D: %5.2f T: %5.2f U: %5.2f" \
                %(self.id, self.wcet, self.wcet*self.coefficient, self.deadline, self.period,self.utilization)