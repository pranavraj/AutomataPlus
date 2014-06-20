import AutomataRead
from Automata_Reach import reach_Automata
def check(List1,List2):
    for term in List1:
        if term in List2:
            return 1
    return 0


def check_Empty(StateList,Accepted,Initial):

    if(Accepted == []):
        return "Language accepts empty language"
    else:
        flag = 0
        for state in Initial:
            if(StateList[state].Final==1):
                return "Language accepts epsilon"
                exit(0)
        for state in StateList:
            if state.Initial == 1:
                next_States = reach_Automata(StateList,state)
                flag = check(next_States,Accepted)
                if(flag==1):
                    return "Automata accepts some language"

        return "Automata has empty language"

if __name__ == "__main__":
    StateList,Accepted,Initial = AutomataRead.FileRead('DFA.txt')
    check_Empty(StateList,Accepted,Initial)
