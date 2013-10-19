'''
Created on 22-July-2010

@author: Naman
'''
import Check_Grammar

def Test_Reg(Grammar):
    Right_linear = Check_Grammar.isRightLinear(Grammar)
    if Right_linear[0] == True:
        Grammar.linear = 1
        return True
    else:
        Left_Linear = Check_Grammar.isLeftLinear(Grammar)
        if Left_Linear[0] == True:
            Grammar.linear = -1
            return True
    return False

def Test_ContextFree(Grammar):
    return Check_Grammar.isContextFree(Grammar)

def Type_Grammar(Grammar):
    isReg = Test_Reg(Grammar)
    if(isReg == False):
        isContextFree = Test_ContextFree(Grammar)
        if(isContextFree == False):
            return "Unrestricted Grammar"
        else:
            return "Grammar is Context Free"
    else:
        if Grammar.linear == -1:
            return "Grammar is Left Linear (Regular and Context Free)"
        elif Grammar.linear == 1:
            return "Grammar is Right Linear (Regular and Context Free)"

"""
Type_Grammar('Grammar.txt')
"""