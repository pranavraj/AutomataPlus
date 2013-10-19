'''
Created on 8-Dec-2010

@author: Swetank
'''
def Automata_unreachable( StateList , Init_State ) :

    ReachableStates = []
    ReachableStates = ReachableStates + Init_State
    ProcessedStates = []

    flag = True

    while( flag ) :

        flag = False
        
        for StNum in ReachableStates :

            if StNum not in ProcessedStates :

                ProcessedStates.append(StNum)
                for NewSt in StateList[ StNum ].next_Transition :
                    
                    if NewSt not in ReachableStates :

                        flag = True
                        ReachableStates.append( NewSt )
    Unreachable_List = []
    for state in StateList:
        if state.StateName not in ReachableStates:
            Unreachable_List.append(state.StateName)        

    return Unreachable_List