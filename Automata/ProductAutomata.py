'''
Created on 05-Dec-2010

@author: Naman
'''
import AutomataRead
"""
Given an input of 2 DFA's this programme returns the product automata of the 2
Both the automata have same input variables
"""
def next_state(instance_list,prev_state,inp_letter):
    return instance_list[prev_state][inp_letter]

def Find_trans(instance_list,prevstate,nextstate):
    list=[]
    if (nextstate) not in instance_list[prevstate-1].transition.values():
        return
    else:
        for trans in instance_list[prevstate-1].transition:
            if instance_list[prevstate-1].transition[trans]==nextstate:
                list.append(trans)
    return list
def product_Automata(File1,File2):
    StateList1,Accepted1,Initial1 = AutomataRead.FileRead(File1)
    StateList2,Accepted2,Initial2 = AutomataRead.FileRead(File2)
    DFA_Product=[]
    Product_Initial = []
    Product_Final = []
    for state in Initial1:
        for state1 in Initial2:
            Product_Initial.append(str(state)+str(state1))
    for state in Accepted1:
        for state1 in Accepted2:
            Product_Final.append(str(state)+str(state1))
    for index in range(len(StateList1)):
        for index1 in range(len(StateList2)):
            transition=[]
            for trans in range(len(StateList1[0].Transition)):
                trans1 = StateList1[index].Transition[trans]
                trans2 = StateList2[index].Transition[trans]
                if trans1 == [-1] or trans2 == [-1]:
                    transition.append([-1])
                else:
                    value = str(trans1[0])+str(trans2[0])
                    transition.append([int(value)])
            new_state = AutomataRead.State()
            new_state.StateName =  str(StateList1[index].StateName) + str(StateList2[index1].StateName)
            new_state.Transition = transition
            if new_state.StateName in Product_Initial:
                new_state.Initial = 1
            if new_state.StateName in Product_Final:
                new_state.Final = 1
            DFA_Product.append(new_state)
    return DFA_Product
"""
Dfa_Product = product_Automata('DFA.txt','DFA1.txt')
for state in Dfa_Product:
    state.display()
"""