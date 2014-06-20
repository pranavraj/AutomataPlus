'''
Created on 08-Dec-2010
@author: Naman
'''
import AutomataRead
from Automata_Useful import Useful_States
# Identifies states that cannot reach accepting states and removes them even unreachable , returns a list of final useful states 

def Useless_States(StateList,Accepted,Initial):
    Useless_List = set()
    UsefulStates = Useful_States(StateList,Accepted)
    #print UsefulStates
    for state in StateList:
        if state.StateName not in UsefulStates and state.StateName not in Accepted and state.StateName not in Initial:
            Useless_List.add(state.StateName) 
    #print Useless_List   
    return Useless_List

def removeUseless_State(StateList,Accepted,Initial):
    UselessStates = Useless_States(StateList,Accepted,Initial)
    if len(UselessStates) == 0:
        print "Automata has no useless state"
        return StateList
    print list(UselessStates),"have been removed"
    StateList = [State for State in StateList if State.StateName not in UselessStates]
    #print StateList
    for state in StateList:
        for index in range(len(state.Transition)):
            transition = state.Transition[index]
            if transition == [-1]:
                continue
            length = len(transition)
            if(length==1 and transition[0] in UselessStates):
                state.Transition[index] = [-1]
            elif(length>1):
                for trans in transition:
                    if trans in UselessStates:
                        transition.remove(trans)
                if(len(transition)==0):
                    transition = [-1]       
            else:
                pass 
        #print "Final transition becomes ",state.Transition
    AutomataRead.update_next_Transition(StateList)

    return StateList

if __name__ == "__main__":
    StateList,Accepted,Initial = AutomataRead.FileRead('DFA.txt')
    StateList =  removeUseless_State(StateList,Accepted)
    for state in StateList:
        state.display()

    
