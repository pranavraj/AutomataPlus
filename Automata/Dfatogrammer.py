'''
@author: Naman
'''
import AutomataRead,string,Grammar.GrammarRead
def convert_Dfa2grammar(StateList):
    Rules = []
    alphadict = dict((x+1,i) for x,i in enumerate(string.ascii_uppercase.replace('S','')))
    variabledict = dict((x+1,i) for x,i in enumerate(string.ascii_lowercase))
    variabledict[0]='%'
    alphadict[0]='S'
    for state in StateList:
        rule = alphadict[state.StateName] + ' -> '
        for index in range(AutomataRead.State.num_variables):
            if(state.Transition[index][0]==-1):
                pass
            else:
                if(index == 0):
                    variable = ''
                    if(len(state.Transition[index]) == 1):
                        rule = rule + variable + alphadict[state.Transition[index][0]]+'|'
                    else:
                        for eps in state.Transition[index]:
                            rule = rule + variable + alphadict[eps]+'|'
                else:
                    variable = variabledict[index]
                    rule = rule + variable + alphadict[state.Transition[index][0]]+'|'
        rule = rule.rstrip('|')
        Rules.append(rule)
    Message = ''
    for rule in Rules:
        Message = Message + str(rule) + '\n'
    return Message
"""
StateList,Accepted,Initial = AutomataRead.FileRead('C:/Python26/Lib/site-packages/Automata/DFA.txt')
print convert_Dfa2grammar(StateList)
"""