import networkx as nx
import matplotlib.pyplot as plt

# Create a graph instance
F = nx.Graph()

# Define vertices
F.add_node("a")
F.add_node("b")
F.add_node("c")
F.add_node("d")
F.add_node("e")
F.add_node("f")
F.add_node("g")

pos = {
    # First tree (T1) in the forest F
    "a": (0, 0.5),
    "b": (0, 0.75),
    "c": (0.5, 0.75),
    "d": (0.25, 1),
    # Second tree (T2) in the forest F
    "e": (0.75, 0.75),
    "f": (1.25, 0.75),
    "g": (1, 1),
}


# Define edges
F.add_edges_from([("a", "b"), ("b", "d"), ("c", "d"), ("e", "g"), ("f", "g")])

# Draw the tree
nx.draw(
    F,
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
