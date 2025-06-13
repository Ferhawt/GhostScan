import networkx as nx
import matplotlib.pyplot as plt

def draw_network_graph(connections):
    G = nx.Graph()
    for node1, node2 in connections:
        G.add_edge(node1, node2)
    nx.draw(G, with_labels=True)
    plt.show()
