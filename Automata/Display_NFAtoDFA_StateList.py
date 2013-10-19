'''
Created on 04-Jan-2011

@author: Naman
'''
# displays the automata
import pydot,os,string
def Conv(StateName):
    if type(StateName).__name__ == 'int':
        return [StateName]
    Temp = []
    for state in StateName:
        if state == '[' or state == ']' or state == ' ' or state == ',':
            continue
        Temp.append(int(state))
    return Temp
def display(StateList,filename):
    alphabet_list = [i for i in string.ascii_lowercase]
    alphabet_list.insert(0, '%')
    graph = pydot.Dot(graph_type='digraph',ranksep = 1,fontsize = 50,nodesep = .25)
    List_nodes = []
    List_names = []
    for state in StateList:
        state.display()
        List_names.append(Conv(state.StateName))
    for state in StateList:
        if state.Final == 0:
            if state.Initial == 1:
                List_nodes.append(pydot.Node(str(state.StateName),shape = "ellipse", style="filled", fillcolor="turquoise"))
            else:
                List_nodes.append(pydot.Node(str(state.StateName),shape = "circle", style="filled", fillcolor="white"))
        else:
            if state.Initial == 1:
                List_nodes.append(pydot.Node(str(state.StateName),shape = "ellipse", style="filled", fillcolor="sienna"))
            else:
                List_nodes.append(pydot.Node(str(state.StateName),shape = "doublecircle", style="filled", fillcolor="sienna"))
    for node in List_nodes:
        graph.add_node(node)
    count = 0
    print "Names of nodes are ",List_names
    for state in StateList:
        print "Consider state",state.StateName
        letter_count = 0
        for transition in state.Transition:
            print "Consider transition : " , transition

            if transition == [-1]:
                letter_count += 1
                continue
            else:
                if letter_count == 0:
                    string1 = "&#949;"
                else:
                    string1 = alphabet_list[letter_count]
                for value in range(len(List_names)):
                    if List_names[value] == transition:
                        val = value
                graph.add_edge(pydot.Edge(List_nodes[count], List_nodes[val],label=string1,len=1.5))
            letter_count += 1
        count += 1
    graph.write(os.getcwd()+"\\"+filename,format = 'png')

    #Image.open('C:\Users\Naman\Desktop\example2_graph.png','r').show()
