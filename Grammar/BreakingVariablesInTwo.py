'''
Created on 22-Dec-2010

@author: Naman
'''
import GrammarRead,copy,re
from Grammar_Functions import isTerminal
def convert_Grammar(Grammar):
    """
    Converts all the productions of grammar into 2 parts like Chomsky Normal Form
    """
    Grammar1 = copy.deepcopy(Grammar)
    dict_g = Grammar1.dict_grammar
    for state in Grammar.dict_grammar:
        #print "state is ",state
        count = 1
        dict_g[state] = []
        for num in xrange(len(Grammar.dict_grammar[state])):
            rule = Grammar.dict_grammar[state][num]
            #print "rule is ",rule
            length = len(rule)
            if length == 1:
                dict_g[state].append(rule)
            elif length == 2:
                variable = ''
                for index in range(length):
                    if isTerminal(Grammar,rule[index]):
                        new_var = state + "_" + str(count)
                        Grammar1.states.append(new_var)
                        count = count+1
                        dict_g[new_var] = [rule[index]]
                        variable = variable + new_var
                    else:
                        variable = variable + rule[index]
                dict_g[state].append(variable)
            else:
                variable = ''
                for index in range(length):
                    if isTerminal(Grammar,rule[index]):
                        new_var = state + "_" + str(count)
                        Grammar1.states.append(new_var)
                        count = count+1
                        dict_g[new_var] = [rule[index]]
                        variable = variable + new_var
                    else:
                        variable = variable + rule[index]
                # variable is now a string of states 
                List_variable = re.findall("[A-Z]_[0-9]+|[A-Z]", variable) 
                #print variable,List_variable
                index = 1
                new_var = state + "_" + str(count)
                dict_g[state].append(List_variable[0] + new_var)
                count += 1
                while True:
                    if index == len(variable)-2:
                        dict_g[new_var] = [variable[index] + variable[index+1]]
                        break
                    else:
                        index = index + 1
                        prev_var = new_var
                        new_var = state + '_' + str(count)
                        count += 1
                        dict_g[prev_var] = [ variable[index] + new_var ]  
    return Grammar1
"""
Grammar = GrammarRead.read_grammar('Grammar.txt')
Grammar.display()
Grammar = convert_Grammar(Grammar)
Grammar.display()
"""