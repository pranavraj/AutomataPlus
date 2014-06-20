import AutomataRead
def automata_Complement(StateList,Accepted,Initial):
    String = ""
    TotalStates = list(range(AutomataRead.State.num_states))
    Accepted_Complement = list(set(TotalStates).difference(Accepted))
    for state in StateList:
        if state.Final == 1:
            String = String + str(state.StateName) + " was earlier an accepting state so it is being converted to non accepting one \n"
            state.Final = 0
        else:
            String = String + str(state.StateName) + " was earlier a non accepting state so it is being converted to accepting one \n "
            state.Final = 1
    return StateList,Accepted_Complement,Initial,String

if __name__ == "__main__":
    StateList,Accepted,Initial = AutomataRead.FileRead('DFA.txt')
    StateList,Accepted_Complement,Initial = automata_Complement(StateList)
    for state in StateList:
        state.display()
