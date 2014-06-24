from AutomataRead import FileRead
import itertools
from pprint import pprint

def enum(**enums):
    return type('Enum', (object,), enums)

OPERATORS = enum(Kleene=1, Union=2, Concatenation=3)

class REobject:
    
    def __init__(self, operator , *operands):
        self.operator = None
        self.operands = None
        self.addOperator(operator, operands)
        
        
    def addOperator(self, operator, *operands):
        self.operator = operator
        if self.operator == OPERATORS.Kleene:
            self.operands = operands[0]
        else:
            self.operands = operands
    
    



Reg = {}    # Reg[(a,b)] represents regular expression from a to b

def addBracket(expression):
    return "(" + expression + ")"

def joinRegex(regexA, joinOperator, regexB = None):
    if joinOperator == OPERATORS.Concatenation:
        assert regexB
        return regexA + regexB
    elif joinOperator == OPERATORS.Union:
        assert regexB
        return addBracket(regexA) + "|" + addBracket(regexB) 
    elif joinOperator == OPERATORS.Kleene:
        assert not regexB
        return addBracket(regexA) + "*"
    else:
        raise Exception("joining regex not possible")

def createGraph(stateList, initState):

    numStates = stateList[0].num_states
    numVariables = stateList[0].num_variables
    
    graph = [[[] for i in range(numStates)] for j in range(numStates)]
    
    alphabets = ['$'] + list(map(chr, range(ord('a'), ord('z')+1))) 
    
    if numVariables > len(alphabets):
        raise Exception("Too many variables")
    
    for state in stateList:
        for varIndex in range(numVariables):
            if state.Transition[varIndex] != [-1]:
                for outEdge in state.Transition[varIndex]:
                    graph[state.StateName][outEdge].append(alphabets[varIndex])
    
    return graph

def reJoin(operA, operB, operC):
    if operA == [] or operB == [] or operC == []:
        return []
    return ["".join(l) for l in list(itertools.product(operA, ["(" + l + ")*" for l in operB], operC))]

def createRE(stateList, initState, finalStates):
    
    Rij = createGraph(stateList, initState)
    
    numStates = stateList[0].num_states
    numVariables = stateList[0].num_variables
    
    Rij_ = [[[] for i in range(numStates)] for j in range(numStates)]
    
    for iter in range(stateList[0].num_states-1):
        for i in range(numStates):
            for j in range(numStates):
                Rij_[i][j] = Rij[i][j] + sum(
                                             [reJoin(Rij[i][k], Rij[k][k], Rij[k][j]) for k in range(numStates)],
                                             [])
        Rij = Rij_
        Rij_ = [[[] for i in range(numStates)] for j in range(numStates)]
        
    return set(
               sum(
                   list(Rij[i][j] for i,j in itertools.product(initState,finalStates)
                        ),
               []
               )
               )
    
        
if __name__ == "__main__":
    StateList, AccpStates, InitialStates = FileRead('DFA.txt')
    l = createRE(StateList, InitialStates, AccpStates)
    for i in l:
        print i