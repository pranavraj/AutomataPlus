'''
Created on 06-Dec-2010
@author: Naman
'''
from Grammar_Functions import isEpsilonProduction,isReducibletoEpsilonProduction
def canAdd(Grammar,Epsilon_States):
    """
    Returns a list where the first value is whether a state can be added such that it has an epsilon rule and second value is that of the state
    """
    for state in Grammar.dict_grammar.keys():
        if state not in Epsilon_States and isEpsilonState(state,Grammar,Epsilon_States)==True:
            return [True,state]
    return [False]

def isEpsilonState(state,Grammar,Epsilon_States):
    """
    Returns whether a state can go to epsilon whether directly or through transitions
    """
    if isEpsilonProduction(Grammar.dict_grammar[state]) == True:
        return True
    if isReducibletoEpsilonProduction(state,Grammar,Epsilon_States) == True:
        return True
    return False
def getEpsilonStates(Grammar):
    """
    returns a set of all the states that can reach epsilon
    """
    Epsilon_States = set() # contains states that directly contibute to epsilon transition
    while True:
        val = canAdd(Grammar,Epsilon_States)
        if val[0] == True:
            state = val[1]
            Epsilon_States.add(state)
        else:
            break
    return Epsilon_States

def identifyEpsilon(Grammar):
    """
    Returns states that can reach epsilon and new grammar with direct epsilon productions removed
    """ 
    Epsilon_States = getEpsilonStates(Grammar) 
    return Epsilon_States,Grammar



