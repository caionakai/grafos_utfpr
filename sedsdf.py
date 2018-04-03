import networkx as nx

#create graph
G=nx.Graph()

#add Node
G.add_node(1, cor='branco')
G.add_node(2, cor='branco')
G.add_node(3, cor='branco')
#link Nodes
G.add_edge(1, 2)
G.add_edge(1, 3)

#G.nodes.data()

for number_of_node_adj,b in G.adj[2].items():
	print(number_of_node_adj)
	

#nodes(G)
#print (G.nodes.data())
#complete_graph(n, create_using=None)

#add list of nodes
#G.add_nodes_from([2,3])




#print ("Numero de nodes: ", G.number_of_nodes())

	
	