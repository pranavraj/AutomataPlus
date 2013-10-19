'''
Created on 16-Dec-2010

@author: Naman
'''
import GrammarRead,string,Grammar_Functions,copy
from Exceptions.Grammar_Exception import isNotRightLinear
from Check_Grammar import isRightLinear
def convert_FSA(Grammar):
    grammar_state = {}
    grammar_terminal = {}
    automata = {}
    alphadict = dict((i+1,x) for i, x in enumerate(string.ascii_lowercase))
    alphadict[0] = '%'
    count = 0
    for terms in Grammar.terminals:
        grammar_terminal[terms] = count
        count += 1
    count = 0
    transition = {}
    print Grammar.dict_grammar
    for states in Grammar.dict_grammar:
        grammar_state[states] = count
        count += 1
    grammar_state['%'] = count
    #print grammar_state
    #print grammar_terminal
    for num in range(Grammar.num_terminals+1):
        transition[alphadict[num]] = []
    #print transition
    for states in Grammar.dict_grammar:
        automata[grammar_state[states]] = copy.copy(transition)
        for rule in Grammar.dict_grammar[states]:
            length = len(rule)
            if rule == '%':
                automata[grammar_state[states]][alphadict[grammar_state[states]]] = grammar_state['%']
            elif length == 2 and Grammar_Functions.num_terminal(Grammar, rule) < 2:
                #print 'initial state is ',[grammar_state[states]],'transition is',alphadict[grammar_terminal[rule[0]]+1],'final state is ',grammar_state[rule[1]]
                automata[grammar_state[states]][alphadict[grammar_terminal[rule[0]]+1]] = grammar_state[rule[1]]
            elif length == 1:
                #print 'initial state is ',[grammar_state[states]],'transition is',alphadict[grammar_terminal[rule[0]]+1],'final state is ',grammar_state['%']
                automata[grammar_state[states]][alphadict[grammar_terminal[rule[0]]+1]] = grammar_state['%']
            elif length == Grammar_Functions.num_terminal(Grammar, rule):
                automata[grammar_state[states]][rule] = grammar_state['%']
            else:
                automata[grammar_state[states]][rule[:length-2]] = grammar_state[rule[length-1]]
    return automata
def RightLineartoFSA(File):
    Grammar = GrammarRead.read_grammar(File)
    value = isRightLinear(Grammar)
    if(not(value[0])):
        raise isNotRightLinear(Grammar,value[1])
    else:
        print convert_FSA(Grammar)
"""
RightLineartoFSA('Grammar.txt')
"""