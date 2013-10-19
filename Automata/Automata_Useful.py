'''
Created on 09-Dec-2010

@author: Naman
'''
from Automata_Reach import reach_Automata
# returns all the useful states ie all those that are not a trap a state
def Useful_States(StateList,Accepted):
    Useful_List = []
    Useful_List = Useful_List + Accepted
    for state in StateList:
        next_state = reach_Automata(StateList,state)
        for Acptstate in Accepted:
            if Acptstate in next_state:
                Useful_List.append(state.StateName)
    return Useful_List