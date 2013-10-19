'''
Created on 16-Dec-2010

@author: Naman
'''
class isNotRestricted(Exception):
    def __init__(self,Grammar):
        self.mssg = "Grammar has length greater than 1 on the left side "
        self.str = ''
        for keys in Grammar.dict_grammar:
            if len(keys)>1:
                self.str = self.str + keys + '  '
            
    def __str__(self):
        string =  self.mssg + self.str
        return string
    
class isNotRightLinear(Exception):
    def __init__(self,Grammar,val):
        self.mssg1 = "Grammar is not Right Linear - all the variables on right side of the rule should be states \n"
        self.val = val
        self.mssg2 = "Check out rule "
    
    def __str__(self):
        string =  self.mssg1 + self.mssg2 + self.val
        return string
        
class isNotLeftLinear(Exception):
    def __init__(self,Grammar,val):
        self.mssg1 = "Grammar is not Left Linear - all the variables on left side of the rule should be states \n"
        self.val = val
        self.mssg2 = "Check out rule "
    
    def __str__(self):
        string =  self.mssg1 + self.mssg2 + self.val
        return string
        
class IllegalProductionException(Exception):
    def __init__(self,rule,letter):
        self.mssg1 = "This production has variables that are neither states nor terminals\n"
        self.mssg2 = "Check out variable " + letter + " in " + rule
    def __str__(self):
        string =  self.mssg1 + self.mssg2
        return string  
        