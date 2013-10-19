'''
Created on 09-Jan-2011

@author: Naman
'''
import AutomataRead,string
alphadict = dict((x, i+1) for i, x in enumerate(string.ascii_lowercase))
alphadict['%'] = 0
def nextState(StateList,prev_state,inp_letter):
    index = StateList[prev_state].Transition[alphadict[inp_letter]]
    value = StateList[prev_state].Transition[alphadict['%']]
    if value == [-1]:
        pass
    else:
        index.extend(value)
    if(index == [-1]):
        return None
    else:
        return index
def inside(List1,List2):
    for num in List1:
        if num in List2:
            return 1
def word_Accept(StateList,Accepted,Initial,word):
    for num in Initial:
        state = StateList[num]
        curr_state = [state.StateName]
        for letter in word:
            if len(curr_state)==1:
                next_state = nextState(StateList,curr_state[0],letter)
            else:
                states = set()
                for state in curr_state:
                    val = nextState(StateList,state,letter)
                    if val == None:
                        pass
                    else:
                        for value in val:
                            states.add(value)
                next_state = list(states)
            curr_state = next_state
        if inside(curr_state,Accepted) == 1:
            return "Word gets accepted"
            exit()
    return "Word does not get accepted"
