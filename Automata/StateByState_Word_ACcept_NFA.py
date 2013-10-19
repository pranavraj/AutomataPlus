'''
Created on 09-Jan-2011

@author: Naman
'''
import AutomataRead,string,copy
alphadict = dict((x, i+1) for i, x in enumerate(string.ascii_lowercase))
alphadict['%'] = 0
def nextState(StateList,prev_state,inp_letter):
    index = StateList[prev_state].Transition[alphadict[inp_letter]]
    if(index == [-1]):
        return None
    else:
        return index
def inside(List1,List2):
    for num in List1:
        if num in List2:
            return 1
def word_Accept(StateList,Accepted,Initial,word):
    string = ''
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
            mssg =  "For letter - " + letter + " we reach " + str(next_state)
            string = string + '\n' + mssg
            curr_state = next_state
        if inside(curr_state,Accepted) == 1:
            string = string + '\n' + "Word gets accepted"
            return string
    string = string + '\n' + "Word does not get accepted"
    return string