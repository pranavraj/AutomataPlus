'''
Created on 15-Dec-2010

@author: Naman
'''
from Exceptions.Grammar_Exception import isNotRestricted
from Grammar_Functions import isState,containsStates,num_terminal
def OneVar_LHS(Grammar):
    LHS_Grammar = Grammar.dict_grammar.keys()
    for rule in LHS_Grammar:
        length = len(rule)
        if length != 1 or (len(rule)==1 and isState(Grammar,rule)==False):
            return False
    return True

def isLeftLinear(Grammar):
    if OneVar_LHS(Grammar) == False:
        raise isNotRestricted(Grammar)
    for state in Grammar.dict_grammar:
        for rule in Grammar.dict_grammar[state]:
            if rule == '%':
                pass
            else:
                variable = containsStates(Grammar,rule)
                if variable == [] and len(rule)== num_terminal(Grammar,rule):
                    pass
                elif len(variable) > 1 or isState(Grammar,rule[0]) == False:
                    return [False,rule]
                
    return [True]       

def isRightLinear(Grammar):
    if OneVar_LHS(Grammar) == False:
        raise isNotRestricted(Grammar)
    for state in Grammar.dict_grammar:
        for rule in Grammar.dict_grammar[state]:
            #print "rule is ",rule
            if rule == '%':
                pass
            else:
                variable = containsStates(Grammar,rule)
                #print "variables in it are ",variable
                if variable == [] and len(rule)== num_terminal(Grammar,rule):
                    pass
                elif len(variable) > 1 or isState(Grammar,rule[-1]) == False:
                    return [False,rule]
    return [True]

def isRegular(Grammar):
    return (isLeftLinear(Grammar) or isRightLinear(Grammar))

def isContextFree(Grammar):
    if OneVar_LHS == False:
        raise isNotRestricted(Grammar)
    else:
        return True