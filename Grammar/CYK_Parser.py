#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Naman
#
# Created:     14-01-2011
# Copyright:   (c) Naman 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import Grammar.GrammarRead as GrammarRead
import Grammar.remove_Epsilon as remove_Epsilon
import Grammar.isCNF as isCNF
from Grammar.removeUnit import removeUnit
import Grammar.CNF_Converter as CNF_Convert

def row_One(Grammar,Check_Str):
    X = {}
    i = 1
    for letter in Check_Str:
        flag = 0
        for state in Grammar.dict_grammar:
            if letter in Grammar.dict_grammar[state]:
                try:
                    X[(i,i)].add(state)
                except KeyError:
                    X[(i,i)] = set([state])
                flag = 1
        i += 1
        if flag == 0:
            return False
    return X

def Calculate_all(Grammar,X,String):
    length = len(String)
    for num_times in range(length-1):   # first row has been calculated so only len(word) - 2 have to be calculated
        increment = num_times+1    # increment among the strings will increase as row number increases
        start = 1
        end = start + increment
        while(end<=length):
            #print "Computing X",start,end
            X[(start,end)] = set()
            for k in range(start,end):
                #print "Checking for these productions"
                for val1 in X[(start,k)]:
                    for val2 in X[(k+1,end)]:
                        prod = val1+val2
                        #print prod
                        for state in Grammar.dict_grammar:
                            if prod in Grammar.dict_grammar[state]:
                                X[(start,end)].add(state)
            #print "We get ",X[(start,end)]
            end += 1
            start += 1
    return X
def cyk_Grammar(Grammar,Check_Str):
    if (isCNF.isCNF(Grammar) == False):
        Grammar = CNF_Convert.convert_CNF(Grammar)
        #print "New Grammar is",Grammar.dict_grammar
    dict_grammar,states,terminals=Grammar.dict_grammar,Grammar.states,Grammar.terminals
    terminals.append('%')
    length = len(Check_Str)
    X = row_One(Grammar,Check_Str)
    if X == False:

        N = len( Check_Str )
        RetList = []
        for Xindex in range(N) :

            Temp = []
            for Yindex in range(N) :
                Temp.append("x")

            RetList.append(Temp)

        return "It is not",RetList
    
    X = Calculate_all(Grammar,X,Check_Str)
    Y = {}
    for element in X.keys():
        Y[element] = str(list(X[element]))
    print Y
    Output = DispAdapter( Y , len(Check_Str) )
    
    if Grammar.startvariable in X[(1,len(Check_Str))]:
        return "It is",Output
    else:
        return "It is not",Output

def DispAdapter( InpDict , N ) :

    RetList = []
    for Xindex in range(N) :

        Temp = []
        for Yindex in range(N) :
            Temp.append("x")

        RetList.append(Temp)

    for KEY in InpDict :

        RetList[ N-(KEY[1]-KEY[0])-1 ][ KEY[0]-1 ] = InpDict[ KEY ]

    print RetList
    return RetList
"""

Grammar = GrammarRead.read_grammar('C:/Python26/Lib/site-packages/Grammar/Grammar.txt')
print cyk_Grammar(Grammar,'abab')
"""
