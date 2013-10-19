'''
Created on 22-Dec-2010

@author: Naman
'''
from Grammar_Functions import hasUnitProduction,isState
def identifyUnit(Grammar):
    """
    Identifies the dictionary of unit productions and returns this dictionary and number of unit productions
    """
    Unit = {}
    for state in Grammar.dict_grammar:
        Unit[state] = set()
        if hasUnitProduction(Grammar.dict_grammar[state],Grammar) == True:
            for rule in Grammar.dict_grammar[state]:
                if len(rule)==1 and isState(Grammar,rule):
                    Unit[state].add(rule)
    return Unit
"""
Grammar = GrammarRead.read_grammar('Grammar.txt')
print identifyUnit(Grammar)
"""