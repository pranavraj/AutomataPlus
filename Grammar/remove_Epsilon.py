'''
Created on 22-Dec-2010

@author: Naman
'''
from identify_Epsilon import identifyEpsilon
import Grammar.GrammarRead as GrammarRead
def rule_clearer(rule,state,start):
    """
    Given a rule and a state that has epsilon transition this function returns a set of rules with the state changed to epsilon
    """
    index = rule.find(state, start)
    if index < 0:
        return set([rule])
    else:
        return set.union(rule_clearer(rule, state, index+1), rule_clearer(rule[:index]+rule[index+1:], state, index))

def remove_Epsilon(Grammar):
    Temp_dict = {}
    eps_State,Grammar = identifyEpsilon(Grammar)
    remove_State = []
    #print "Epsilon states are " , eps_State
    for state in eps_State:
        if(len(Grammar.dict_grammar[state])==0):
            remove_State.append(state)
    for state in remove_State:
        del Grammar.dict_grammar[state]
        for state1 in Grammar.dict_grammar:
            temp = []
            for rule in Grammar.dict_grammar[state1]:
                rule = rule.replace(state,'')
                temp.append(rule)
            Grammar.dict_grammar[state1] = temp
        Grammar.states.remove(state)
    for state in Grammar.dict_grammar:
        #print "Consider state ",state
        Temp_dict[state] = []
        for production in Grammar.dict_grammar[state]:
            #print "Consider production ",production
            flag = 0
            for eps_state in eps_State:
                if str(eps_state) in production:
                    flag = 1
                    List = rule_clearer(production,str(eps_state),0)
                    try:
                        List.remove('')
                    except KeyError:
                        pass
                    Temp_dict[state].extend(list(List))
                    continue
            if flag == 0:
                Temp_dict[state].append(production)
    for state in Temp_dict:
        for production in Temp_dict[state]:
            if len(production) == 2:
                for term in range(2):
                    if production[term] in eps_State:
                        if term == 0:
                            Temp_dict[state].append(production[1])
                        else:
                            Temp_dict[state].append(production[0])
        #print Temp_dict[state]
        Temp_dict[state] = list(set(Temp_dict[state]))
    Grammar.dict_grammar = Temp_dict
    return Grammar
"""
Grammar = GrammarRead.read_grammar('C:/Python26/Lib/site-packages/Grammar/Grammar.txt')
print Grammar.dict_grammar
grammar = remove_Epsilon(Grammar)
print grammar.dict_grammar
"""