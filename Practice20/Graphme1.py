import matplotlib.pyplot as plt
import networkx as nx

input = open('Fruit.txt', 'r')
list = input.readlines()
Gra=[['0']*3 for n in range (len(list))]
for i in range (len(list)):
    list[i] = list[i].rstrip()
    a,b,c = list[i].split()
    Gra[i][0], Gra[i][1],Gra[i][2] = a,b,int(c)
    print(list[i])
print(Gra)
print(len(Gra))

input.close()


G = nx.Graph()
for i in range (len(Gra)):
    G.add_edge(Gra[i][0],Gra[i][1],weight =Gra[i][2])
#G.add_edge('a','b',weight=0.6)
#G.add_edge('a','c',weight=0.2)
#G.add_edge('c','d',weight=0.1)
#G.add_edge('c','e',weight=0.7)
#G.add_edge('c','f',weight=0.9)
#G.add_edge('a','d',weight=0.3)

elarge = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] > 400]
esmall = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=399]

pos = nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=70)

# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=6)
nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')

# labels
nx.draw_networkx_labels(G,pos,font_size=5,font_family='sans-serif')

plt.axis('off')
plt.show() # display