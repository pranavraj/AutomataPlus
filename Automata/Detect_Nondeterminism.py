import AutomataRead
def detect_Nondet(StateList):
    non_det = {}    
    for state in StateList:
            index = 0
            trans1 = []
            for trans in state.Transition:
                if len(trans) > 1:
                    if(index == 0):
                        trans1.append('%')
                    else:
                        trans1.append(chr(ord('a')+index-1))
                index += 1
            if len(trans1) == 0:
                pass
            else:
                non_det[state.StateName] = trans1
    return non_det            

if __name__ == "__main__":    
    StateList,Accepted,Initial = AutomataRead.FileRead("DFA.txt")        
    detect_Nondet(StateList)