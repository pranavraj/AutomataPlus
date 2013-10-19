'''
Created on 16-Dec-2010

@author: Naman
'''
class ParenthesisNotBalanced(Exception):
    def __init__(self,string):
        self.mssg = "The entered string does not have balanced parenthesis"
        self.val = string
    
    def __str__(self):
        string =  self.mssg1 + self.val
        return string