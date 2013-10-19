'''
Created on 02-Dec-2010

@author: Naman
'''
import GrammarRead,Grammar_Reach
from Grammar_Functions import generateTerminal,isTerminal
def generate_term(Grammar,state):
        term = generateTerminal(Grammar,state)
        if term == True:
            return True
        else:
            for productions in Grammar.dict_grammar[state]:
                for rule in productions:
                    if isTerminal(rule) == True:
                        pass
                    else:


def Grammar_empty_check(Grammar):
    if('%' in Grammar.dict_grammar[Grammar.startvariable]):
        return "Grammar is accepting epsilon"
    else:
        if(generate_term(Grammar,Grammar.startvariable)):
            return "Grammar is accepting some language"
        else:
            return "Grammar accepts empty language"
"""
Grammar = GrammarRead.read_grammar('C:/Python26/Lib/site-packages/Grammar/Grammar.txt')
print Grammar_empty_check(Grammar)
"""