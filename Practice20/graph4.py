import networkx as nx
import matplotlib.pyplot as plt


def file_into_tuple_list(fname):
    Graph = nx.Graph()
    with open(fname) as f:
        for line in f:
            if line:
                a, b, w = line.split()
                Graph.add_edge(a, b, weight=float(w))
    return Graph


def bfs(G, start):
    queue = [start]
    tree = nx.Graph()
    G = nx.to_dict_of_dicts(G)
    used = {start}
    while queue:
        curr = queue.pop(0)
        for n in G[curr]:
            if n not in used:
                used.add(n)
                tree.add_edge(curr, n, weight=G[curr][n]['weight'])
                queue.append(n)
    return tree

def components(G):
    result = set()
    used = []
    for i in G:
        if i not in used:
            wing = bfs(G,i)
            for element in wing:
                if element not in used:
                    used.append(element)
            result.add(wing)
    return result
Graph = file_into_tuple_list('Fruit.txt')
for t in components(Graph):
    nx.draw_shell(t)
plt.show()
Number_of_trees = len(components(Graph))
print('The number of trees is',Number_of_trees)
if Number_of_trees > 1:
    print('The graph is not connected')
if Number_of_trees == 1:
    print('The graph is connected')