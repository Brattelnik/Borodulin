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

def dejkstra(G,start):
    shortest_path = {vertex:float('inf') for vertex in G}
    shortest_path[start] = 0
    queue =[start]
    while queue:
        current = queue.pop()
        for neighbour in G[current]:
            offering_shortest_path = shortest_path[current] + G[current][neighbour]['weight']
            if offering_shortest_path < shortest_path[neighbour]:
                shortest_path[neighbour] = offering_shortest_path
                queue.append(neighbour)
    return shortest_path

def shortest(G, start, finish):
    D = dejkstra(G, start)
    t = finish
    path=[]
    while t:
        path.append(t)
        t = D[t][1]
    return path[::-1]

Graph = file_into_tuple_list('Fruit.txt')
print('Select the start city')
start_city= input()
print('Select the finish city')
finish_city = input()
print(shortest(Graph,start_city,finish_city))
