import networkx as nx

G=nx.Graph()

teste = 1

G.add_node(1, time='teste')
G.add_node(2)

G.add_edge(1, 2)

teste = teste +1

G.nodes[1]['time']=teste

#print (G.nodes.data())
print (G.nodes[1]['time'])


def DFS-Visit(G, u):
	tempo = tempo + 1
	G.nodes[u]['descoberta'] = tempo
	G.nodes[u]['cor'] = "cinza"
	
