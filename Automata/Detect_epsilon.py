def detect_Epsilon(StateList):
    eps_states = {}
    for state in StateList:
        eps_state = []
        if(state.Transition[0] != [-1]):
            for eps in state.Transition[0]:
                eps_state.append(eps)
        if len(eps_state)==0:
            pass
        else:
            eps_states[state.StateName] = eps_state
    return eps_states        

"""
StateList,Accepted,Initial = AutomataRead.FileRead("DFA.txt")          
detect_Epsilon(StateList)
"""