'''
@author: Naman
'''
import AutomataRead,string
alphadict = dict((x, i+1) for i, x in enumerate(string.ascii_lowercase))
def nextState(prev_state,inp_letter):
    index = prev_state.Transition[alphadict[inp_letter]]
    if(index == -1):
        return None
    else:
        return index
def inside(List1,List2):
    for num in List1:
        if num in List2:
            return 1
def word_Accept(File,word):
    StateList,Accepted,Initial = AutomataRead.FileRead(File)
    reached = 0
    for state in Initial:
        prev_state = StateList[state]
        for letter in word:
            if(reached == 0):
                next_state = (nextState(prev_state,letter))
                if(next_state != None):
                    prev_state=StateList[next_state[0]]
        if(inside(next_state,Accepted)==1):
            reached = 1
        else:
            reached = 0
    if(reached == 1):
        print "Word gets accepted"
    if(reached == 0):
        print "Word does not get accepted"

word_Accept('DFA.txt','bbbbbbbb')