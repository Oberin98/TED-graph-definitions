import networkx as nx
import matplotlib.pyplot as plt

# Create a graph instance
T = nx.Graph()

# Define vertices
T.add_node(1)
T.add_node(2)
T.add_node(3)
T.add_node(4)
T.add_node(5)
T.add_node(6)

# Define vertices position
pos = {
    1: (0.5, 0.25),
    2: (1, 0.25),
    3: (0.75, 0.5),
    4: (0.75, 0.75),
    5: (1.25, 0.75),
    6: (1, 1),
}

# Define edges
T.add_edges_from([(1, 3), (2, 3), (3, 4), (4, 6), (5, 6)])

# Draw the tree
nx.draw(
    T,
    pos,
    with_labels=True,
    font_weight="bold",
    node_color="white",
    edgecolors="black",
    edge_color="black",
    node_size=800,
    linewidths=1,
)

plt.show()
