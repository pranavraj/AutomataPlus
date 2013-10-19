"""Created by Pranav Raj on 20/3/2012 """

import RE
from SubNFA import *

#special characters

Plus = '+'
Star = '*'
Epsilon = '%'

StateInitials = 'Q'
StateIndex = 0

def SortLen( Array ): 

    #sort Array based on length , in decreasing order
    Array.sort(key = len,reverse = True)

def NextState():

    global StateIndex
    nextState = StateInitials + str(StateIndex)
    StateIndex += 1

def Mapping( String , Replacements ):

    Alphabets = [ chr(n) for n in range(ord('A'), ord('Z')+1)] + [ chr(n) for n in range(ord('a'), ord('z')+1)]
    AlphaIndex = 0
    AlphaMap = {}
    
    for replacement in Replacements:
        
        while Alphabets[AlphaIndex] in String : AlphaIndex += 1
        AlphaMap[replacement] = Alphabets[AlphaIndex]
        AlphaIndex += 1
        
    return AlphaMap       

def FormatAsterisk( String ):

    Patterns = RE.FindAllWithSpecialChar(String,"*")
    SortLen(Patterns)

    for SubPattern in Patterns:

        ReplacementPattern = "(" + SubPattern + ")"
        String = String.replace(SubPattern,ReplacementPattern)

    return String
        
def FormatPlus( String ):

    Patterns = RE.FindAllWithSpecialChar(String,"+")
    SortLen(Patterns)

    for SubPattern in Patterns:

        ReplacementPattern = "(" + SubPattern + ")"
        String = String.replace(SubPattern,ReplacementPattern)

    return String

def FormatOr( String ):

    Patterns = RE.FindAllAroundSpecialChar(String)
    SortLen(Patterns)

    for SubPattern in Patterns:

        ReplacementPattern = "(" + SubPattern + ")"
        String = String.replace(SubPattern,ReplacementPattern)

    return String
        
def Format( String ):

    def reform(string):
        return "(" + string + ")"

    Reps = []
    
    R = RE.FindAll(String)
    Reps  += [r for r in R]

    return Reps[::-1]

def Map( String ):

    Replacements = Format(String)
    #the order in list matters, so we need to maintain the order of list while replacing
    WordsMapping = Mapping(String , Replacements)

    AlreadyReplaced = []
    StringMapping = {}
    
    for word in Replacements:

        replacement = WordsMapping[word]

        for rep in AlreadyReplaced:
            word = word.replace(rep[0],rep[1])

        String = String.replace(word,replacement)
        StringMapping[replacement] = word
        AlreadyReplaced.append((word,replacement))

    return String , StringMapping

def ConstructNFA( String, StringMapping ):
    
    LenString = len(String)
    NFAs = []
    alphaindex = 0

    while (alphaindex < LenString):
       
        Atom = String[alphaindex]

        if Atom == "*" or Atom == "+" or Atom == "|" : 

            alphaindex += 1
            continue

        if alphaindex < LenString-1 and String[alphaindex+1] == "*":

            if Atom in StringMapping :

                AtomNFA = ConstructNFA( StringMapping[Atom] , StringMapping )
                AtomNFA.Create( "*")
                NFAs.append(AtomNFA)

            else:

                AtomNFA = SubNFA()
                AtomNFA.Create( Atom )
                AtomNFA.Create( "*" )
                NFAs.append(AtomNFA)

        elif alphaindex < LenString-1 and String[alphaindex+1] == "+":

            if Atom in StringMapping :

                AtomNFA = ConstructNFA( StringMapping[Atom] , StringMapping )
                AtomNFA.Create( "+")
                NFAs.append(AtomNFA)

            else:

                AtomNFA = SubNFA()
                AtomNFA.Create( Atom )
                AtomNFA.Create( "+" )
                NFAs.append(AtomNFA)

        elif alphaindex < LenString-2 and String[alphaindex+1] == "|":
            
            A = Atom
            B = String[alphaindex+2]
            
            if A in StringMapping:

                A_NFA = ConstructNFA(StringMapping[A],StringMapping)

            else:

                A_NFA = SubNFA()
                A_NFA.Create(A)

            if B in StringMapping:

                B_NFA = ConstructNFA(StringMapping[B],StringMapping)

            else:

                B_NFA = SubNFA()
                B_NFA.Create(B)

            NFAs.append(A_NFA)
            alphaindex += 1
                
        else:

            if Atom in StringMapping :

                print "Atom : " , Atom
                AtomNFA = ConstructNFA ( StringMapping[Atom] , StringMapping)
                NFAs.append(AtomNFA)

            else:

                AtomNFA = SubNFA()
                AtomNFA.Create( Atom  )
                NFAs.append(AtomNFA)

        alphaindex += 1

    NFA = AtomNFA.Join(NFAs)
    return NFA

def ReToNfa ( RegEx ):

    RegEx , REMapping = Map(RegEx)
    
    #format REMapping; remove brackets from the values
    for key in REMapping:
        value = REMapping[key]
        REMapping[key] = REMapping[key][1:len(value)-1]
    
    NFA = ConstructNFA(RegEx,REMapping)
    NFA.Reform()
    NFA.Print()

def Reform ( String ):

    #precedence order : * > + > |
    String = FormatAsterisk(String)
    String = FormatPlus(String)
    String = FormatOr(String)
    return String


ReToNfa(Reform("a*bc|d"))

    
    


