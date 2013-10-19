"""Created by Pranav on 20/03/2012 """

from pprint import pprint

StateNum = 0

class SubNFA():

    def __init__(self):

        global StateNum

        self.Star = "*"
        self.Plus = "+"
        self.Or = "|"
        self.Epsilon = "%"
        self.NoOp = ""
        self.StateInitials = "Q"
        self.StartState = ""
        self.FinalState = ""
        self.States = []
        self.Transitions = {}

    def Create(self,Operator):

        global StateNum        

        if Operator == self.Star:

            self.Transitions[self.StartState] = list(set( self.Transitions.get(self.StartState, []) + [(self.Epsilon,self.FinalState)]))
            self.Transitions[self.FinalState] = list(set( self.Transitions.get(self.FinalState, []) + [(self.Epsilon,self.StartState)]))

        elif Operator == self.Plus:

            self.Transitions[self.StartState] = list(set( self.Transitions.get(self.StartState, [])))
            self.Transitions[self.FinalState] = list(set( self.Transitions.get(self.FinalState, []) + [(self.Epsilon,self.StartState)]))
                
        else:

            self.StartState = self.StateInitials + str(StateNum)
            self.States.append(self.StateInitials + str(StateNum))
            StateNum += 1
            self.FinalState = self.StateInitials + str(StateNum)
            self.States.append(self.StateInitials + str(StateNum))
            StateNum += 1
            self.Transitions[self.StartState] = [(Operator,self.FinalState)]

    def JoinByOr( self , NFA ):

        global StateNum
        _StartState = self.StateInitials + str(StateNum)
        self.States.append(self.StateInitials + str(StateNum))
        StateNum += 1
        _FinalState = self.StateInitials + str(StateNum)
        self.States.append(self.StateInitials + str(StateNum))
        StateNum += 1

        self.States += NFA.States
        self.Transitions.update(NFA.Transitions)

        self.Transitions[_StartState] = []
        self.Transitions[_StartState].append((self.Epsilon,NFA.StartState))
        self.Transitions[_StartState].append((self.Epsilon,self.StartState))


        self.Transitions[NFA.FinalState] = list(set(self.Transitions.get(NFA.FinalState,[]) + [(self.Epsilon,_FinalState)]))
        self.Transitions[self.FinalState] = list(set(self.Transitions.get(self.FinalState,[]) + [(self.Epsilon,_FinalState)]))
        self.StartState = _StartState
        self.FinalState = _FinalState
      
    def JoinTwo (self, NFA_A , NFA_B ):

        """We have to join NFA_A and NFA_B """

        
        NFA = SubNFA()
        NFA.StartState = NFA_A.StartState
        NFA.FinalState = NFA_B.FinalState
        
        #doing simple work ; needs to be improved <Pranav/>
        NFA.States = NFA_A.States + NFA_B.States
        NFA.States.remove(NFA_B.StartState)
        NFA.Transitions = dict(NFA_A.Transitions.items() + NFA_B.Transitions.items())

        for Key in dict(NFA_B.Transitions.items() + NFA_B.Transitions.items()):
            Values = []
            for ValueEle in NFA.Transitions[Key]:
                if ValueEle[1] == NFA_B.StartState:
                    Values.append((ValueEle[0],NFA_A.FinalState))
                else:
                    if ValueEle[1] in NFA.States : Values.append(ValueEle)
            if Key == NFA_B.StartState: Key = NFA_A.FinalState
            NFA.Transitions[Key] = list(tuple(NFA.Transitions.get(Key,[]) + Values))

        del NFA.Transitions[NFA_B.StartState]

        return NFA

    def Join (self,  NFAs ):

        """returns the output of joining all the nfas in NFAs """
        NFALen = len(NFAs)
        if NFALen == 1:
            return NFAs[0]
        PreJoinedNFA = NFAs[0]
        for NFAIndex in range(1,NFALen):
            PreJoinedNFA = self.JoinTwo(PreJoinedNFA,NFAs[NFAIndex])
        return PreJoinedNFA

    def Reform(self) :

        StateIndex = 0
        _StateInitials = "S"
        _States = []
        _StartState = ""
        _FinalState = ""
        _Transitions = {}
        _StateMapping = {}

        Keys = self.Transitions.keys()
        Keys.sort()
        for Key in Keys:
            if Key not in _StateMapping :
                _StateMapping[Key] =  _StateInitials + str(StateIndex)
                _States.append(_StateMapping[Key])
                StateIndex += 1
            _Transitions[_StateMapping[Key]] = []
            for Values in self.Transitions[Key]:
                if Values[1] in self.Transitions or Values[1] == self.FinalState :
                    
                    if Values[1] not in _StateMapping:
                        _StateMapping[Values[1]] =  _StateInitials + str(StateIndex)
                        _States.append(_StateMapping[Key])
                        StateIndex += 1
                        
                    _Transitions[_StateMapping[Key]].append((Values[0],_StateMapping[Values[1]]))

        #remove duplicate element from transitions
        for Key in _Transitions:
            _Transitions[Key] = list((set(_Transitions[Key])))
            
        _FinalState =  _StateMapping[self.FinalState]
        _StartState =  _StateMapping[self.StartState]
        
        self.States = _States
        self.Transitions = _Transitions
        self.FinalState = _FinalState
        self.StartState = _StartState            
                
    def Print( self ):
        print "States"
        print "".join(["_"]*10)
        pprint(self.States)
        print 
        print "Start State"
        print "".join(["_"]*10)
        pprint(self.StartState)
        print 
        print "Final State"
        print "".join(["_"]*10)
        pprint(self.FinalState)
        print 
        print "Transitions"
        print "".join(["_"]*10)
        pprint(self.Transitions)
        



       

        
            

            
            
            
        

        
