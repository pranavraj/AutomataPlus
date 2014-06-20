def changeformat(mydict,final,start):
    K=mydict.keys()
    K.sort()
    alpha=[]
    states=[]
    states.extend(K)
    for k in K :
        for j in mydict[k] :
            if j[0] not in alpha :
                alpha.append(j[0])
            if j[1] not in states:
                states.append(j[1])

    alpha.sort()
    if '%' not  in alpha :
        alpha=['%']+alpha
    else :
        alpha.remove('%')
        alpha=['%']+alpha
    print alpha
    timepass=[]
    for k in alpha  :
        timepass.append('{-1}')

    f1=open ("Temp.aut",'w')

    f1.write( str(len(alpha))+" "+str(len(states)))
    f1.write('\n')
    f1.write ('{'+str(states.index(start))+'}')
    f1.write('\n')

    for m in states:


        insert_lis=[]
        insert_lis.extend(timepass)
        if m in K:
            for m1 in mydict[m]:
                if insert_lis[alpha.index(m1[0])]=='{-1}':
                        insert_lis[alpha.index(m1[0])]="{"+str(states.index(m1[1]))+"}"
                else:
                        insert_lis[alpha.index(m1[0])]='{'+insert_lis[alpha.index(m1[0])].split('{')[-1].split('}')[0]+','+str(states.index(m1[1]))+'}'

        for m in insert_lis:
            f1.write(m+" ")

        f1.write('\n')
    final_states="{"+str(states.index(final[0]))

    for i in range(1,len(final)):
        final_states=final_states+','+str(states.index(final[i]))

    final_states=final_states+"}"
    f1.write(final_states)
    f1.write('\n')
    f1.close()

if __name__ == "__main__":
    di={'A':[['a','A'],['b','B'],['a','C']],'B':[['c','C']]}
    changeformat(di,['C'],'A')
