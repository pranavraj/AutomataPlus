'''
Created on 24-Dec-2010

@author: Naman
'''
from Grammar.Check_Grammar import OneVar_LHS
from Grammar.GrammarRead import read_grammar
from Grammar.remove_Epsilon import remove_Epsilon
from Grammar.BreakingVariablesInTwo import convert_Grammar
from Grammar.removeUnit import removeUnit
from Exceptions.Grammar_Exception import isNotRestricted
def convert_CNF(Grammar):
    if not(OneVar_LHS):
        raise isNotRestricted
    #print "Initial Grammar is ",Grammar.dict_grammar
    Grammar1 = remove_Epsilon(Grammar)
    #print " After removing epsilon ",Grammar1.dict_grammar
    Grammar2 = removeUnit(Grammar1)
    #print "After removing unit ",Grammar2.dict_grammar
    Grammar3 = convert_Grammar(Grammar2)
    #print "After breaking in 2",Grammar3.dict_grammar
    return Grammar3
"""
Grammar = read_grammar('C:/Python26/Lib/site-packages/Grammar/Grammar.txt')
convert_CNF(Grammar)
"""