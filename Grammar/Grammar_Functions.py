'''
Created on 15-Dec-2010

@author: Naman
'''
def generateTerminal(Grammar,state):
    for rule in Grammar.dict_grammar[state]:
        if isTerminal(Grammar,rule) == True:
            return True
    return False

def isState(Grammar,rule):
    """
    Returns whether the rule passed is a state
    """
    if rule in Grammar.states:
        return True
    return False

def isTerminal(Grammar,rule):
    """
    Returns whether the rule passed is a terminal
    """
    if rule in Grammar.terminals:
        return True
    return False

def containsTerminal(Grammar,rule):
    Terminal = []
    for term in Grammar.terminals:
        if term in rule:
            Terminal.append(term)
    return Terminal

def containsStates(Grammar,rule):
    """
    returns the list of states that are in a single rule
    """
    States = []
    for state in Grammar.states:
        if state in rule:
            States.append(state)
    return States

def terminals_RHS(Grammar1,state):
    """
    returns the list of terminals on right side of productions of state
    """
    Terminals = []
    rule = Grammar1.dict_grammar[state]
    for production in rule:
        Terminals.extend(containsTerminal(Grammar1,production))
    return list(set(Terminals))

def num_terminal(Grammar,rule):
    """
    Returns the number of terminal in the rule passed
    """
    count = 0
    for val in rule:
        if val in Grammar.terminals:
            count+=1
    return count

def terminals_LHS(Grammar1,state):
    """
    returns the list of terminals on left side of productions of state
    """
    Terminals = []
    Terminals.extend(containsTerminal(Grammar1,state))
    return list(set(Terminals))

def states_RHS(Grammar1,state):
    """
    returns the list of states on right side of productions of state
    """
    States = []
    rule = Grammar1.dict_grammar[state]
    for production in rule:
        States.extend(containsStates(Grammar1,production))
    return list(set(States))

def states_LHS(Grammar1,state):
    """
    returns the list of states on left side of productions of state
    """
    States = []
    States.extend(containsStates(Grammar1,state))
    return list(set(States))

def hasepsilon_Production(rule):
    """
    Returns if the rules passed have an epsilon production
    """
    for production in rule:
        if production == '%':
            return True
    return False

def hasUnitProduction(rule,Grammar):
    """
    returns True if any rule of the productions passed is a Unit Production
    """
    for production in rule:
        if len(production) == 1 and isState(Grammar,production) == True:
            return True
    return False

def isUnitProduction(production,Grammar):
    """
    returns True if any production passed is a Unit Production
    """
    if len(production) == 1 and isState(Grammar,production) == True:
        return True
    return False

def reach_Grammar(Grammar,state):
    """
    Returns the set of states which the state passed can reach through its productions
    """
    next_states = []
    states = Grammar.states
    trans = set(states_RHS(Grammar,state))
    while(len(trans)!= 0):
        state = trans.pop()
        try:
            states.remove(state)
            next_states.append(state)
            trans.update(set(states_RHS(Grammar,state)))
        except ValueError:
            pass
    return next_states

def leftmost_variable(Grammar,rules):
    """
    Returns the list of left most variables in all the productions passed
    """
    left_var = []
    for rule in rules:
        left_var.append(rule[0])
    return left_var

def isEpsilonProduction(rule):
    """
    Identifies if the productions contain an epsilon transition
    """
    for production in rule:
        if production == '%':
            rule.remove(production)
            return True
    return False

def hasTerminal(rule,Grammar):
    """
    Returns whether the rule has any terminal in it
    """
    for letter in rule:
        if isTerminal(Grammar,letter)==True:
            return True
    return False
def isReducibletoEpsilonProduction(state,Grammar,Epsilon_Set):
    for rule in Grammar.dict_grammar[state]:
        if hasTerminal(rule,Grammar) == True:
            pass
        else:
            flag = 0
            for letter in rule:
                if letter not in Epsilon_Set:
                    flag = 1
            if flag == 1:
                continue
            else:
                return True
    return False