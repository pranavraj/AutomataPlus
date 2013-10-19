'''
Created on 05-Jan-2011

@author: Naman
'''
import pydot,os,string
def display(dictionary,nodes,filename):
    graph = pydot.Dot(graph_type='digraph',ranksep = 1,fontsize = 50,nodesep = .25)
    List_nodes = []
    for state in nodes:
        if state == "Q0" :
            node = pydot.Node(state,shape = "ellipse", style="filled", fillcolor="turquoise")
        elif state == "Q1" :
            node = pydot.Node(state,shape = "doublecircle", style="filled", fillcolor="sienna")
        else:
            node = pydot.Node(state,shape = "circle", style="filled", fillcolor="white")
        List_nodes.append(node)
    for node in List_nodes:
        graph.add_node(node)
    for state in dictionary:
        for transition in dictionary[state]:
            string1 = transition[0]
            if string1 == '%':
                string1 = "&#949;"
            graph.add_edge(pydot.Edge(List_nodes[int(state[1:])], List_nodes[int(transition[1][1:])],label=string1,len = 1.5))
    graph.write(os.getcwd()+"\\"+filename,prog = 'neato',format = 'png')
    #Image.open('C:\Users\Naman\Desktop\example2_graph.png','r').show()


