'''
Created on 17-Dec-2010
@author: Naman
'''
# tells the states that a state of an automata can reach
def reach_Automata(StateList,state):
    total_List = set(xrange(state.num_states))
    next_List = set(state.next_Transition)
    reach_List = set()
    while(len(next_List) != 0):
        state_name = next_List.pop()
        try:
            total_List.remove(state_name)
            reach_List.add(state_name)
            next_List.update(set(StateList[state_name].next_Transition))
        except KeyError:
            pass
    return list(reach_List)