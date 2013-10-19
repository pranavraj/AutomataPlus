'''
Created on 20-July-2010

@author: Naman
'''
import GrammarRead
def reach_variable(list,states):
    variables=[]
    for rule in list:
        for state in states:
            if state in rule:
                variables.append(state)
    return set(variables)

def generate_term(grammar,state,terminal):
    flag=0
    for state in grammar[state]:
        for term in terminal:
            if term == state:
                flag=1
    if flag==1:
        return 1
    else:
        return 0

def set_reachable(grammar,states,temp):
    dict={}
    for state in states:
        dict[state]=0
    flag=0
    next1=[]
    while(flag==0):
        list1=[]
        flag1=0
        for value in temp:
            next1.append(value)
            dict[value]=1
            next=reach_variable(grammar[value],states)
            list1.extend(next.difference(next1))
        for term in list1:
            if dict[term]==0:
                dict[term]=1
                flag1=1
        if flag1==0:
            flag=1
        temp=list1
    return dict

def set_generating(grammar,states,terminal):
    dict={}
    for state in states:
        dict[state]=generate_term(grammar,state,terminal)
    for state in dict:
        list=grammar[state]
        for rule in list:
            flag=1
            if rule == '%':
                continue
            for letter in rule:
                if letter not in terminal and dict[letter]==0:
                    flag=0
            if flag == 1:
                dict[state]=1
                break
    return dict

def reachable_Grammar(Grammar):
    unreachable=[]
    generating=[]
    dict=set_reachable(Grammar.dict_grammar,Grammar.states,[Grammar.startvariable])
    for term in dict:
        if dict[term]==0:
            unreachable.append(term)
    Message1 = "Set of unreachable states is  " + str(unreachable)
    dict=set_generating(Grammar.dict_grammar,Grammar.states,Grammar.terminals)
    for term in dict:
        if dict[term]==1:
            generating.append(term)
    Message2 = "Set of generating states is  " + str(generating)
    return Message1 +'\n'+Message2
"""
reachable_Grammar('Grammar.txt')
"""