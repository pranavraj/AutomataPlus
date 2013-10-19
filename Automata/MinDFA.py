"""
To minimize a given DFA
"""

def DFAAdapter( InpDFA ) :

    for State in InpDFA :
        State.Transition = sum( State.Transition , [] )


def TrapStList( Autom , ReachableSt ) :

    TrapSt = [ ]
    for item in ReachableSt :

        flag = True
        for trans in Autom[ item ].Transition :

            if( (trans != -1) and (trans != item) ) :
                flag = False

        if( flag == True ) : TrapSt.append( item )

    return TrapSt


def RemUnreach( Automaton , Init_State ) :

    ReachableStates = [ ]
    ReachableStates = ReachableStates + Init_State
    ProcessedStates = [ ]

    flag = True

    while( flag ) :

        flag = False

        for StNum in ReachableStates :

            if StNum not in ProcessedStates :
                flag = True
                ProcessedStates.append( StNum )

            for st in Automaton[StNum].Transition :

                if( st not in ReachableStates ) : ReachableStates.append( st )
                    
            ReachableStates.remove( -1 )

    return ReachableStates


def MinimDFA( OrigDFA , AcceptStates , InitState ) :

    Message = ""

    DFAAdapter( OrigDFA )

    ReachSt = RemUnreach( OrigDFA , InitState )
    ReachSt.sort()

    UnReachable = []
    for st in OrigDFA :
        if( st.StateName not in ReachSt ) : UnReachable.append( st.StateName )

    ReachableDFA = []
    for StObj in OrigDFA :

        if StObj.StateName in ReachSt :
            ReachableDFA.append( StObj )

    StatePairs = []

    for state1 in ReachableDFA :

        for state2 in ReachableDFA :

            if( state1.StateName != state2.StateName ) :

                CandidPair = state1 , state2
                CheckPair = tuple( reversed(CandidPair) )

                if CheckPair not in StatePairs :
                    StatePairs.append( CandidPair )


    Distinguish = []
    for pair in StatePairs :

        if( ( (pair[0].StateName in AcceptStates) and (pair[1].StateName not in AcceptStates) ) or
            ( (pair[0].StateName not in AcceptStates) and (pair[1].StateName in AcceptStates) ) ) :

            Pair = pair[0].StateName,pair[1].StateName
            Message += "State Pair :"+str(Pair)+" are distinguished as State(s) <b>"+str(AcceptStates)+"</b>"+" are accepting<br>"
            Distinguish.append( Pair )

    OldDistinguish = []
    while( Distinguish != OldDistinguish ) :

        OldDistinguish = Distinguish

        for pair in StatePairs :

            CondPair = pair[0].StateName , pair[1].StateName
            if( CondPair not in Distinguish ) :

                for counter in range( 0 , len(pair[0].Transition) ) :

                    IncludePair = pair[0].Transition[counter] , pair[1].Transition[counter]
                    ReversePair = tuple( reversed(IncludePair) )

                    if( (IncludePair in Distinguish) or (ReversePair in Distinguish) ) :

                        Distinguish.append( CondPair )
                        Message += "State Pair :"+str(CondPair)+" are distinguished<br>"
                        break

    TrapStates = TrapStList( OrigDFA , ReachSt )

    for st in AcceptStates :
        if ( st in TrapStates ) : TrapStates.remove( st )

    DistPairs = [ ]
    TrapPairs = [ ]
    for pair in Distinguish :

        if( (pair[0] not in TrapStates) and (pair[1] not in TrapStates) ) :
            DistPairs.append( pair )

        else : TrapPairs.append( pair )

    SimPairs = [ ]
    for pair in StatePairs :

        CondPair = pair[0].StateName , pair[1].StateName
        if( (CondPair not in DistPairs) and (CondPair not in TrapPairs) ) :
            SimPairs.append( CondPair )


    OutDFA = [ ]

    for IntSt in InitState :
        if IntSt in TrapStates :

            OrigDFA[IntSt].Transition = [ -1 for x in OrigDFA[IntSt].Transition ]
            OutDFA.append( OrigDFA[IntSt] )

        else :
            for index in TrapStates : OrigDFA.pop( index )

            if( SimPairs == [] ) :

                OutDFA = OrigDFA
                for StObj in OrigDFA :
                    StObj.Transition = [ -1 if x in TrapStates else x for x in StObj.Transition ]


            else :
                for pair in SimPairs :
                    for StObj in OrigDFA :

                        StObj.Transition = [ pair[0] if x == pair[1] else x for x in StObj.Transition ]
                        StObj.Transition = [ -1 if x in TrapStates else x for x in StObj.Transition ]

                        if( StObj.StateName == pair[1] ) : continue

                        else : OutDFA.append( StObj )

    
    for St in OutDFA : St.Transition = map( list , [ (x,) for x in St.Transition ] )

    MinDFA = []
    print "\nMINIMIZED DFA\n"
    for St in OutDFA :

        if( St.StateName in ReachSt ) :

            MinDFA.append( St )
            print St.StateName
            print St.Transition
            print

    print "Reachable States : "+str( ReachSt )
    print "Similar States : "+str( SimPairs )
    print "Trap States : "+str( TrapStates )

    Message += "Similar States : "+str( SimPairs )+"<br>"
    Message += "Trap States : "+str( TrapStates )+"<br>"
    Message += "UnReachable States : "+str( UnReachable )+"<br>"

    return MinDFA , Message
