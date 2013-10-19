
"""Edited on 20/3/2012 by Pranav Raj """

import GrammarRead
import copy
import Grammar_Functions
import Grammar_Reach

def identify_leftrecur(Grammar):

    dict_recursion = {}

    for node in Grammar.dict_grammar:

        print node
        variables = Grammar.states + Grammar.terminals
        flag = False
        
        list_var = Grammar_Functions.leftmost_variable(Grammar, Grammar.dict_grammar[node])
        print list_var
        
        list_var_copy = copy.copy(list_var)
        reachable = set()

        while(len(list_var_copy)!=0):

            var = list_var_copy.pop()

            try:
                
                variables.remove(var)
                
                if Grammar_Functions.isState(Grammar,var) == True:
                    
                    reachable.add(var)
                    list_var_copy.extend(Grammar_Functions.leftmost_variable(Grammar, Grammar.dict_grammar[var]))
                    
            except:
                
                pass

        print reachable

        if node in reachable:
                flag = True

        dict_recursion[node] = flag

    return dict_recursion

if __name__ == "__main__":

    Grammar = GrammarRead.read_grammar('C:/Python26/Lib/site-packages/Grammar/Grammar.txt')
    print identify_leftrecur(Grammar)

