"""
State name starts from 1 to n (StateName+1)
Rijk = Go from i'th state to j'th and the path has no node greater than kth number
"""
import AutomataRead
def next_state(StateList,prev_state,inp_letter):
    return StateList[prev_state][inp_letter]

def Find_trans(StateList,prevstate,nextstate):
    list=[]
    if ([nextstate]) not in StateList[prevstate-1].Transition:
        return
    else:
        for trans in StateList[prevstate-1].Transition:
            if trans==[nextstate]:
                list.append(trans[0])
    return list


def Rij0(i,j,StateList):
    list=Find_trans(StateList,i,j)
    if list == None:
        return 'False'
    else:
        if(len(list)==1):
            return list[0]
        else:
            Str= str(list[0])
            for index in range(1,len(list)):
                Str=Str+'|'+str(list[index])
            return Str

def MakeArray(StateList):
    array={}
    for i in range (1,len(StateList)+1):
        for j in range (1,len(StateList)+1):
            for k in range (0,len(StateList)):
                RExp=str(i)+str(j)+str(k)
                if(i==j and k==0):
                    array[RExp]='e'
                else:
                    if(k==0):
                        array[RExp]=Rij0(i,j,StateList)
                    else:
                        array[RExp]='False'
    Str='1'+str(len(StateList))+str(len(StateList))
    array[Str]='False'
    return array

def Array_change(i,j,k,value,Finalarray):
    if (k==0):
        Finalarray[str(i)+str(j)+str(k)]= Finalarray[str(i)+str(j)+str(k)]+'|'+str(value)


def Parse(R1,R2,R3,R4):
    r1=R1
    r2=R2
    r3=R3
    r4=R4
    if(R1 == 'False'and (R2 == 'False' or R3 == 'False' or R4 == 'False')):
        r1='False'
        r2=r3=r4=''
    else:
        if(R1 == 'False'):
            r1=''
        if(R2 == 'False' or R3 == 'False' or R4 == 'False'):
            r2=r3=r4=''
        if (R2== R3):
            r2=''
        if (R3 == R4):
            r4=''

    return (r1,r2,r3,r4)

def Looping(StateList,Finalarray):
    for state in StateList:
        for trans in state.Transition:
            if trans==[state.StateName]:
                Array_change(state.StateName+1,state.StateName+1,0,trans[0],Finalarray)


def Recursion(StateList,Finalarray):
    for i in range (1,len(StateList)+1):
        for j in range (1,len(StateList)+1):
            for k in range (1,len(StateList)+1):
                #print str(i)+str(j)+str(k)
                R1=str(i)+str(j)+str(k-1)
                R2=str(i)+str(k)+str(k-1)
                R3=str(k)+str(k)+str(k-1)
                R4=str(k)+str(j)+str(k-1)
                S1,S2,S3,S4=Parse(Finalarray[R1],Finalarray[R2],Finalarray[R3],Finalarray[R4])
                if(S1==''):
                    Str='('+S2+'('+'('+S3+')'+'*'+')'+S4+')'+')'
                else:
                    if(S3==''):
                        Str='('+S1+'+'+'('+S2+S4+')'+')'
                    else:
                        Str='('+S1+'+'+'('+S2+'('+'('+S3+')'+'*'+')'+S4+')'+')'
                #print Str
                Finalarray[str(i)+str(j)+str(k)] = Str
    R2=str(1)+str(j-1)+str(j-2)
    R1=str(i)+str(j-1)+str(j-2)
    R3=str(j-1)+str(j-1)+str(j-2)
    R4=str(j-1)+str(j-1)+str(j-2)
    Str='('+Finalarray[R1]+'+'+'('+Finalarray[R2]+'('+Finalarray[R3]+'*'+')'+Finalarray[R4]+')'+')'
    Finalarray['1'+str(len(StateList))+str(len(StateList))]=Str



def Rijk(File):
    StateList,Accepted,Initial = AutomataRead.FileRead('DFA.txt')
    Finalarray=MakeArray(StateList)
    print Finalarray
    #Looping(StateList,Finalarray)                         #Rii0
    #Recursion(StateList,Finalarray) # rest of the expression
    for i in range (1,len(StateList)+1):
        for j in range (1,len(StateList)+1):
            for k in range (0,len(StateList)):
                RExp=str(i)+str(j)+str(k)
                print RExp , "is" , Finalarray[RExp],'\n'
    print "Language of Automata is",Finalarray['1'+str(len(StateList))+str(len(StateList))]

Rijk('DFA.txt')