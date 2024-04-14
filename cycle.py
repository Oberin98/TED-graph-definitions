import networkx as nx
import matplotlib.pyplot as plt

# Create a graph instance
G = nx.Graph()

# Define vertices
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)

# Define edges
G.add_edges_from(
    [(1, 5), (2, 3), (2, 4), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7), (5, 7)]
)

# Define cycle in the graph G
cycle_edges = [(2, 3), (3, 5), (5, 7), (7, 2)]

# Define layout
pos = nx.circular_layout(G)

# Draw the graph
nx.draw(
    G,
    pos,
    with_labels=True,
    font_weight="bold",
    node_color="white",
    edgecolors="black",
    edge_color="lightgray",
    node_size=800,
    linewidths=1,
)

# Draw only the edges to highlight the cycle in the graph G
nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, edge_color="black")

plt.show()
