import networkx as nx
import matplotlib.pyplot as plt


def file_into_tuple_list(fname):

    G = nx.Graph()
    with open(fname) as f:
        for line in f:
            if line:
                a, b, w = line.split()
                G.add_edge(a, b, weight=float(w))
    return G


def drawme(graph, path = []):

    pos = nx.shell_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=500)
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), width=1)
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family='sans-serif')
    nx.draw_networkx_edges(graph, pos, edgelist=[(path[i], path[i+1]) for i
                                                 in range(len(path) - 1)], width=1)
    plt.axis('off')
    plt.show()


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

Graph = file_into_tuple_list('Fruit.txt')
drawme(bfs(Graph, 'Земляничный'))