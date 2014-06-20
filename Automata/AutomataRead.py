import re
from Display_Automata_StateList import display

"""
The file is of the following format
NoofAlphabets(always including epsilon),NumberofStates
InitialStates
Transitions per each alphabet in the form of {} where {-1} shows no transition and the first is always for epsilon {-1} for DFA
AcceptingStates
\n
"""

from Exceptions.Automata_Exception import IllegalTransition

class State(object) :
    """Is a class of State object in an Automata"""
    num_states = 0              # number of states in Automata
    num_variables = 0           # number of states in num_variables
    def __init__(self):
        self.StateName = 0
        self.Final = 0                 # whether it is final or not
        self.Initial = 0               # whether it is an initial state or not
        self.Transition = []           # records the transition in the form of alphabets
        self.next_Transition = []     # records all the states the state can reach

    def display(self):
        print '----------------------------------------------'
        print 'The state number is ' , self.StateName
        print 'Its Transition are' , self.Transition
        if(self.Final==1):
            print 'It is a final state'
        if(self.Initial==1):
            print 'It is an initial state'
        #print self.next_Transition
            
    def numberOfstates(self):
        return State.num_states

    def add_state(self):
        State.num_states += 1

    def remove_state(self):
        State.num_states -= 1

def update_next_Transition(StateList):
    for state in StateList:
        next_trans = []
        for trans in state.Transition:
            next_trans.extend(trans)
        next_trans = list(set(next_trans))
        try:
            next_trans.remove(-1)
        except ValueError:
            pass
        state.next_Transition = next_trans
    return StateList

def FileRead(AutomataFile) :
    DFAFile = open( AutomataFile , 'r' )
    DFALines = DFAFile.readlines()
    AlphaSize1 , NoOfStates = tuple( DFALines[0].split() )
    AlphaSize = int ( AlphaSize1)
    State.num_variables = AlphaSize
    NoOfStates = int ( NoOfStates )
    InitialStates = DFALines[1][1:len(DFALines[1])-2].split(',')
    InitialStates = map(int,InitialStates)
    AccpStates = DFALines[ len(DFALines) - 1][ 1 : len(DFALines[ len(DFALines) - 1]) - 2 ].split(',')
    AccpStates = map( int , AccpStates )
    StateList = []

    def ConvInteger( List ) :
        List = map( int , List )
        for item in List:
            if item >= NoOfStates:
                raise IllegalTransition(item)
        return List
    for statenumber in range( 2 , NoOfStates + 2 ) :
        DFALines[statenumber] = re.sub( '{' , '' , DFALines[statenumber] )
        DFALines[statenumber] = re.sub( '}' , '#' , DFALines[statenumber] )
        DFALines[statenumber] = re.sub( "\s+" , '' , DFALines[statenumber] )

        DFALines[statenumber] = DFALines[statenumber].rstrip('\n')
        DFALines[statenumber] = DFALines[statenumber].rstrip('#')

        Transitions = DFALines[statenumber].split('#')
        TransitionList = [ Transt.split(',') for Transt in Transitions]
        TransitionList = map ( ConvInteger , TransitionList )
        NewState = State()
        State.add_state(NewState)
        NewState.StateName = statenumber-2
        NewState.Transition = TransitionList
        State_Trans = list(set(map(int, ','.join(Transitions).split(','))))
        try:
            State_Trans.remove(-1)
        except ValueError:
            pass
        NewState.next_Transition = State_Trans
        if(statenumber-2 in AccpStates):
            NewState.Final = 1
        if(statenumber-2 in InitialStates):
            NewState.Initial = 1
        StateList.append( NewState )

    DFAFile.close()

    return StateList,AccpStates,InitialStates
if __name__ == "__main__":
    StateList,AccpStates,InitialStates = FileRead('DFA.txt')
    display(StateList)
