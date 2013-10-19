import copy,AutomataRead
def check(List1,List2):
    for term in List1:
        if term in List2:
            return 1
    return 0
def move(StateList,curr_state,inputindex):
    next_state = []
    for state in curr_state:
        next = StateList[state].Transition[inputindex]
        if (next == [-1]):
            pass
        else:
            next_state.extend(next)
    return list(set(next_state))

def epsilon_closure(StateList,curr_states):
    stack=copy.copy(curr_states)
    while(len(stack)!=0):
        state1=[stack.pop()]
        epsilon_state=move(StateList,state1,0)
        for state in epsilon_state:
            if state not in curr_states:
                curr_states.append(state)
                stack.append(state)
    return curr_states

def transform_Dfa(StateList,initial,Accepted):
    String = "<html> <body> <font size= 5 face= 'Georgia, Arial' color= ' maroon ' >"
    flag = 0
    for state in StateList:
        for trans in state.Transition:
            if len(trans) > 1:
                flag = 1
        if state.Transition[0] != [-1]:
            flag = 1
    if flag == 0:
        return StateList,"<p>Already a DFA<p><br>"
    DFAstates = []
    DFAList = []
    Initial = copy.copy(initial)
    dfa_start = epsilon_closure(StateList,initial)
    String = String + " We start with epsilon closure of start state ie " + str(Initial) + " = " + str(dfa_start) + "<br>"
    DFAstates.append(dfa_start)
    mark = []         # check the states in new DFA have been used or not
    mark.append(0)
    try:
        while(True):
            i = mark.index(0)
            mark[i]=1
            state=DFAstates[i]
            String = String + " We consider state " + str(state) +"<br>"
            trans=[]
            trans.append([-1])     # initially append -1 for epsilon as the resultant is a DFA.
            for alphabet in range(1,AutomataRead.State.num_variables):
                next_state=epsilon_closure(StateList,move(StateList,state,alphabet))
                if len(next_state)==0:
                    trans.append([-1])
                else:
                    next_state=list(set(next_state)) # no need
                    if next_state not in DFAstates:
                        String = String +  " We get a new state concatinated with its epsilon closure for transition " + chr(ord('a')+alphabet-1) + ": " + str(next_state) + " and append it for further use"+"<br>"
                        DFAstates.append(next_state)
                        mark.append(0)
                    trans.append(next_state[0:])
            new_state = AutomataRead.State()
            new_state.StateName = str(state)
            new_state.Transition = trans
            if(state==dfa_start):
                new_state.Initial=1
            flag = check(state,Accepted)
            if(flag == 0):
                String += "<p> The state " +str(state) + " does not consist of accepting states in " + str(Accepted) + " so it is NOT an accepting state <p>"+"<br>"
                new_state.Final = 0
            else:
                String += " <p> The state " +str(state) + " consist of accepting states in " + str(Accepted) + " so it too is accepting state" + "<br>"
                new_state.Final = 1
            DFAList.append(new_state)
    except ValueError:
        String = String + "</font></body></html>"
        for state in DFAList:
            state.display()
        return DFAList,String
"""
StateList,Accepted,Initial = AutomataRead.FileRead('NFA.txt')
DFAList = transform_Dfa(StateList,Initial,Accepted)
for state in DFAList:
    state.display()
"""