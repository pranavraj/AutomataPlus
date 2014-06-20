'''
Created on 08-Dec-2010
@author: Naman
'''
import AutomataRead
from Automata_Unreachable import Automata_unreachable

def remove_unreachable(StateList,Initial,num_Var):
    List = Automata_unreachable(StateList,Initial)
    print "Unreachable states are ",List
    if List == []:
        pass
    else:
        for state in StateList:
            if state.StateName in List:
                StateList.remove(state)

    return StateList

if __name__ == "__main__":
    StateList,Accepted,Initial = AutomataRead.FileRead('DFA.txt')
    StateList = remove_unreachable(StateList,Initial,AutomataRead.State.num_variables)
    for state in StateList:
        state.display()
