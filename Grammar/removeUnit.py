'''
Created on 22-Dec-2010

@author: Naman
'''
import Grammar.GrammarRead as GrammarRead
from Grammar.identifyUnitProduction import identifyUnit
from Grammar.Grammar_Functions import isUnitProduction
import copy
def removeUnit(Grammar):
    """
    returns the Grammar with all the unit productions removed
    """
    Unit = identifyUnit(Grammar)
    Dependency = {}
    for state in Unit:
        variables = copy.copy(Grammar.states)
        Dependency[state] = copy.copy(Unit[state])
        variables.remove(state)
        while(len(Unit[state])!=0):
            value = Unit[state].pop()
            try:
                variables.remove(value)
                Unit[state] = Unit[state].union(Unit[value])
                Dependency[state] = Dependency[state].union(Unit[value])
            except ValueError:
                pass
    Grammar1 = copy.deepcopy(Grammar)
    Grammar1.dict_grammar = {}
    for state in Grammar.states:
        Grammar1.dict_grammar[state] = []
    for state in Grammar.dict_grammar:
        for rule in Grammar.dict_grammar[state]:
            if isUnitProduction(rule,Grammar) == False:
                Grammar1.dict_grammar[state].append(rule)
        for variable in Dependency[state]:
            for rule in Grammar.dict_grammar[variable]:
                if isUnitProduction(rule,Grammar) == False:
                    Grammar1.dict_grammar[state].append(rule)
    for state in Grammar1.dict_grammar:
        Grammar1.dict_grammar[state] = list(set(Grammar1.dict_grammar[state]))
    return Grammar1
"""
Grammar = GrammarRead.read_grammar('Grammar.txt')
print removeUnit(Grammar)
"""