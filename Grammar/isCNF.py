#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Naman
#
# Created:     14-01-2011
# Copyright:   (c) Naman 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import Grammar.GrammarRead as GrammarRead
import Grammar.remove_Epsilon as remove_Epsilon
import Grammar.Grammar_Functions as Gram_Func
def isCNF(Grammar):
    Grammar.terminals.append('%')
    for state in Grammar.dict_grammar:
        for rules in Grammar.dict_grammar[state]:
            if(len(rules)>2):
                return False
            elif(len(rules)==2):
                for terminal in rules:
                    if(Gram_Func.isState(Grammar,terminal) == False):
                        return False
            else:
                if(Gram_Func.isTerminal(Grammar,rules)==False):
                    return False
    return True
"""
Grammar = GrammarRead.read_grammar('C:/Python26/Lib/site-packages/Grammar/Grammar.txt')
print isCNF(Grammar)
"""
