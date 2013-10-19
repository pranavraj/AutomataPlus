'''
Created on 08-Dec-2010

@author: Naman
'''
import Alphabet_Dict,AutomataRead,remove_Useless_States
from nfa_to_re import letmetest
def identifyRemovable(dict_DFA,Accepted,Initial):
    Removable = []
    for state in dict_DFA:
        if state not in Accepted and state not in Initial:
            Removable.append(state)
    return Removable

def convertFSA_RE(dict_DFA,Accepted,Initial):
    Accpt = []
    for state in Accepted:
        Accpt.append(str(state))
    value = str(Initial[0])
    States = []
    print dict_DFA
    for state in dict_DFA:
        States.append(str(state))
    print dict_DFA,value,Accpt,States
    string = letmetest(dict_DFA,value,Accpt,States)
    return string

def state_elimination(StateList,Accepted,Initial):
    if(len(Initial)!=1):
        return "Incorrect Input"
    StateList = remove_Useless_States.removeUseless_State(StateList, Accepted,Initial)
    dict_DFA = Alphabet_Dict.convert_to_dict(StateList)
    string = convertFSA_RE(dict_DFA,Accepted,Initial)
    return string
"""
StateList,Accepted,Initial = AutomataRead.FileRead('C:/Python26/Lib/site-packages/Automata/DFA.txt')
state_elimination(StateList,Accepted,Initial)
"""