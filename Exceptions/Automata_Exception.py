'''
Created on 16-Dec-2010

@author: Naman
'''

class IllegalTransition(Exception):
    def __init__(self,val):
        self.val = val
        self.mssg1 = "Illegal Transition : State "
        self.mssg2 = " does not exist"
    def __str__(self):
        string =  self.mssg1 + str(self.val) + self.mssg2
        return string