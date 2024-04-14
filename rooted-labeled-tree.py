import networkx as nx
import matplotlib.pyplot as plt

# Create a graph instance
T = nx.Graph()

# Define vertices
T.add_node("a")
T.add_node("b")
T.add_node("c")
T.add_node("d")
T.add_node("e")
T.add_node("f")

# Define vertices position
pos = {
    "a": (0.5, 0.25),
    "b": (1, 0.25),
    "c": (0.75, 0.5),
    "d": (0.75, 0.75),
    "e": (1.25, 0.75),
    "f": (1, 1),
}

# Define edges
T.add_edges_from([("a", "c"), ("b", "c"), ("c", "d"), ("d", "f"), ("e", "f")])

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
