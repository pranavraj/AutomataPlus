import copy,AutomataRead,string
def automata_Reverse(StateList,Accepted,Initial):
    for state in StateList:
        state.display()
    alphabet_list = dict((x+1,i) for x,i in enumerate(string.ascii_lowercase))
    alphabet_list[0] = ' % '
    String = ""
    """
    for state in StateList:
        state.display()
    """
    Rev_Initial = copy.deepcopy(Accepted)
    Rev_Accepted = copy.deepcopy(Initial)
    Rev_State = []
    count = 0
    for state in StateList:
        new_state = AutomataRead.State()
        new_state.StateName = count
        count += 1
        if state.Final == 1:
            String = String + str(state.StateName) + " was earlier an accepting state so it now converts into an initial one"
            new_state.Initial = 1
        if state.Initial == 1:
            String = String + str(state.StateName) + " was earlier an initial state so it now converts into an accepting one"
            new_state.Final = 1
        trans1 = []
        for trans in state.Transition:
            trans1.append([-1])
        new_state.Transition = trans1
        Rev_State.append(new_state)
    for length in range(len(StateList)):
        state = StateList[length]
        trans = state.Transition
        for index in range(len(state.Transition)):
            if(trans[index][0]==-1):
                pass
            else:
                if(Rev_State[trans[index][0]].Transition[index][0]==-1):
                    Rev_State[trans[index][0]].Transition[index].pop()
                    String = String + str(trans[index][0]) + "goes to " + str(state.StateName) + " For " + alphabet_list[index] + ' \n '
                    Rev_State[trans[index][0]].Transition[index].append(state.StateName)
                else:
                    Rev_State[trans[index][0]].Transition[index].append(state.StateName)
    AutomataRead.update_next_Transition(Rev_State)
    for state in Rev_State:
        state.display()
    return Rev_State,Rev_Accepted,Rev_Initial,String
if __name__ == "__main__":
    StateList,Accepted,Initial = AutomataRead.FileRead('DFA.txt')
    FSA_reverse,Rev_Accpt,Rev_Initial = automata_Reverse(StateList,Accepted,Initial)
    for state in FSA_reverse:
        state.display()
