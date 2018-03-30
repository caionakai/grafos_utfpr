#GET ORDER
import networkx as nx


G = nx.Graph()

G.add_node(1)
G.add_node(2)

G.add_edge(1,2)

G.add_node(3)
G.add_node(4)

G.add_edge(1,3)
G.add_edge(2,4)

print G.number_of_nodes()
print G.number_of_edges()
