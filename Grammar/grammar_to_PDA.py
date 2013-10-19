
"""Edited on 20/3/2012 by Pranav Raj """

import Grammar.GrammarRead as GrammarRead

def convert2PDA(Grammar):

    grammar = Grammar.dict_grammar

    transitions = ''
    transition = ''

    for state in grammar.keys():

        transition = "(q , % , "+str(state)+" ) = { "
        state_index = 0
        transitions_state =len(grammar[state])
        
        if transitions_state == 1 :
            transition = transition + " ( q , " + str( grammar[state][state_index] ) + " ) }"

        else:
            
            while state_index < len(grammar[state])-1:
                
                transition = transition + " ( q , " + str( grammar[state][state_index] ) + " ), "
                state_index += 1
                
            transition = transition + "( q , " + str(grammar[state][j]) + " ) }" + "\n"
            
        transitions = transitions + '\n' + transition
        
    for term in Grammar.terminals:
        transitions = transitions + '\n' + str("( q , "+term+' , '+term+" ),") +"=" +"{ ( q , % ) }" + "\n"

    return transitions


if __name__ == "__main__":

    Grammar = GrammarRead.read_grammar('C:/Python26/Lib/site-packages/Grammar/Grammar.txt')
    print convert2PDA(Grammar)



