def findthenext(path , ele, needtofind,inlist):
    global graph
    global list,path_to_be_removed
    #print list

    #print "path :",path
    #print "ele :",ele
    nxt=[]

    if (ele not in inlist or needtofind==ele) and ele in graph.keys():
        inlist.append(ele)
        nxt1=graph[ele]
        path1=[]
        for nxt in nxt1:
            if needtofind == nxt[1]:
                if [ele,nxt] not in path_to_be_removed:
                    path1.append([ele,nxt])
                    #nxt1.remove(nxt)
                list.append(path+nxt[0])

            if nxt[1] != needtofind and nxt[0] not in path :

                findthenext(path+nxt[0],nxt[1],needtofind,inlist)
    return list





def clickme(dict,revdict,ele):
    #print "looking for ",ele
    for km in dict.keys():
        meralist=[]
        lost=[]
        lost.extend(dict[km])
        for mk in lost :
            if mk[1] == km :
                revdict[mk[1]].remove([mk[0],km])
                dict[km].remove(mk)
                meralist.append(mk[0])
        if meralist!=[]:
            for jazz in dict[km]:
                revdict[jazz[1]].remove([jazz[0],km])
            str2=makekliene(meralist)
            for jazz in dict[km] :

                revdict[jazz[1]].append(["("+str2+")*"+jazz[0],km])
                jazz[0] = "("+str2+")*"+jazz[0]

    li2=[]

    li2.extend(dict[ele])
    li1=[]
    li1.extend(revdict[ele])

    p=0
    ho=0
    for l1 in li1 :
        if ho == 1:
            break
        for l2 in li2 :
            print "appending to ",l1[1]," :",[l1[0]+l2[0],l2[1]]
            dict[l1[1]].append([l1[0]+l2[0],l2[1]])
            print "rev appending to ",l2[1]," :",[l1[0]+l2[0],l1[1]]
            revdict[l2[1]].append([l1[0]+l2[0],l1[1]])
            #print "done for ",l1,l2
            p=p+1
            if ho==1:
                break

    for j in li1:
        print "removing frm dic "," :",j[1] , [j[0],ele]
        dict[j[1]].remove([j[0],ele])
    for j in li2:
        print "removing frm revdic "," :",j[1] , [j[0],ele]
        revdict[j[1]].remove([j[0],ele])
    del dict[ele]
    del revdict[ele]
    for km in dict.keys():
        meralist=[]
        lost=[]
        lost.extend(dict[km])
        for mk in lost :
            if mk[1] == km :
                revdict[mk[1]].remove([mk[0],km])
                dict[km].remove(mk)
                meralist.append(mk[0])
        if meralist!=[]:
            for jazz in dict[km]:
                revdict[jazz[1]].remove([jazz[0],km])
            str2=makekliene(meralist)
            for jazz in dict[km] :

                revdict[jazz[1]].append(["("+str2+")*"+jazz[0],km])
                jazz[0] = "("+str2+")*"+jazz[0]

def makekliene(lis):


    if len(lis)==1:
        return lis[0]

    else:
        pv=lis[0]

        for i in range(1,len(lis)):
            if lis[i]!='%':
                pv=pv+'|'+lis[i]
        return pv









def detect_cycle(graph):

    global list
    global path_to_be_removed
    list=[]
    path_to_be_removed=[]

    for k in graph.keys():

        findthenext('',k,k,[])


        if list!=[]:
            print list
            str0="("+makepair(list)+")*"
            # you can also cover str0 with()*
            for m in graph[k]:
                m[0]=str0+m[0]
            #graph[k].append([str0,k])


        list=[]
    return graph













def letmetest(dict,start,end,states,make=True):
    if make:

        dict['Start']=[['%',start]]
        start='Start'

        for ko in end :
            if ko in dict.keys():
                dict[ko].append(['%','End'])
            else:
                dict[ko]=[['%','End']]
        end= ['End']




    revdict={}
    for k in dict.keys():
        for m in dict[k] :
            if m[1] in revdict.keys():
                if [m[0],k] not in revdict[m[1]]:
                    revdict[m[1]].append([m[0],k])
            else:
                revdict[m[1]]=[[m[0],k]]


    for km in dict.keys():
        meralist=[]
        lost=[]
        lost.extend(dict[km])
        for mk in lost :
            if mk[1] == km :
                revdict[mk[1]].remove([mk[0],km])
                dict[km].remove(mk)
                meralist.append(mk[0])
        if meralist!=[]:
            for jazz in dict[km]:
                revdict[jazz[1]].remove([jazz[0],km])
            str2=makekliene(meralist)
            for jazz in dict[km] :

                revdict[jazz[1]].append(["("+str2+")*"+jazz[0],km])
                jazz[0] = "("+str2+")*"+jazz[0]


    # to look into * problem


    single_transition_ele=[]

    for k in dict.keys():
        if len(dict[k])==1:
            try:
                if  len(revdict[k])==1 :
                    single_transition_ele.append(k)
            except:
                pass



    for k in single_transition_ele:
        str1a=revdict[k][0][0]
        str1b=dict[k][0][0]
        str1=str1a+str1b
        st1=revdict[k][0][1]
        st2=dict[k][0][1]
        del dict[k]
        del revdict[k]
        dict[st1].remove([str1a,k])
        revdict[st2].remove([str1b,k])
        dict[st1].append([str1,st2])
        revdict[st2].append([str1,st1])


    mystates=[]
    mystates.extend(states)
    for k in single_transition_ele:
        mystates.remove(k)
    try:
        mystates.remove(start)
    except:
        pass
    try :
        mystates.remove('End')
    except:
        pass

    for j in mystates:




        clickme(dict,revdict,j)
        #mystates.remove(j)
    if len(dict.keys())!=1:
        return ("Unexpected error . Please report this error to pranav ")
    output=[]
    for j in dict[dict.keys()[0]]:
        output.append(j[0])

    op="|".join(output)
    return "("+op+")"



    li=[]
    print dict


