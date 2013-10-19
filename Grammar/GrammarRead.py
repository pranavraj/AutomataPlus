'''
Created on 04-Dec-2010

@author: Naman
'''
""" Following file is to check whether a given word exists in the grammer production or not

    The format of the text file will be as follows
    First line will have all the states
    Second line will have all the terminals
    For each state mentioned above there is a corresponding rule given after in format S -> SS|AB|0
"""
from Exceptions.Grammar_Exception import IllegalProductionException
class Grammar(object):
    num_states = 0
    num_terminals = 0
    linear = 0    # will be -1 for left linear 1 for right linear and 2 for regular
    def __init__(self):
        self.startvariable = 'S'
        self.states = []
        self.terminals = []
        self.dict_grammar = {}

    def set_numOfstates(self):
        Grammar.num_states = len(self.states)
    def set_numOfterm(self):
        Grammar.num_terminals = len(self.terminals)
    def display(self):
        Message = "Grammar is as follows \n"
        for state in self.dict_grammar:
            rules = ''
            for rule in self.dict_grammar[state]:
                rules = rules + ' | ' + rule
            rules = rules.lstrip('|')
            Message = Message + state +' -> ' + rules + '\n'
        return Message

def read_grammar(File):
    file1=open(File,'r')
    data=file1.readlines()
    Grammar1 = Grammar()
    G_state = data[0].rstrip()
    G_terminal = data[1].rstrip()
    Grammar1.states = G_state.split(',')
    Grammar1.terminals=G_terminal.split(',')
    Grammar1.set_numOfstates()
    Grammar1.set_numOfterm()
    for index in range(2,2+Grammar1.num_states):
        rule=data[index].rstrip()
        for letter in rule:
            if letter == '-' or letter == '>' or letter == '|' or letter == '%':
                pass
            elif letter not in Grammar1.states and letter not in Grammar1.terminals:
                raise IllegalProductionException(rule,letter)
        lhs = rule[:rule.find('-')]
        rhs = rule[rule.find('>')+1:]
        rhs=rhs.split('|')
        Grammar1.dict_grammar[lhs]=rhs
    return Grammar1
"""
Grammar = read_grammar('C:/Python26/Lib/site-packages/Grammar/Grammar.txt')
print Grammar.dict_grammar,Grammar.terminals,Grammar.display()
"""