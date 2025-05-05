import networkx as nx
import matplotlib.pyplot as plt

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def kruskal(graph, numVertices):
    edges = []
    for i in range(numVertices):
        for j in range(i + 1, numVertices):
            if graph[i][j] != 0:
                edge = Edge(i, j, graph[i][j])
                edges.append(edge)

    edges.sort()

    parent = list(range(numVertices))
    mst = []
    total_weight = 0

    for edge in edges:
        src_parent = find(parent, edge.src)
        dest_parent = find(parent, edge.dest)
        if src_parent != dest_parent:
            mst.append(edge)
            parent[src_parent] = dest_parent
            total_weight += edge.weight

    return mst, total_weight

def visualize_graph(graph, mst, V):
    G = nx.Graph()
    
    # Add nodes
    for v in range(V):
        G.add_node(v)

    # Add all edges
    for i in range(V):
        for j in range(i + 1, V):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    # Positions for nodes
    pos = nx.spring_layout(G)

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=12)

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Highlight the MST edges in red
    mst_edges = [(e.src, e.dest) for e in mst]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=3, edge_color='red')

    # Title
    plt.title("Graph with Minimum Spanning Tree (MST)")

    # Display the graph
    plt.show()

# Get number of edges and vertices
E = int(input("Enter the number of edges: "))
V = int(input("Enter the number of vertices: "))

# Initialize an empty graph
graph = [[0 for _ in range(V)] for _ in range(V)]

print("Enter edges in the format: src dest weight")
for _ in range(E):
    src, dest, weight = map(int, input().split())
    graph[src][dest] = weight
    graph[dest][src] = weight  # Assuming an undirected graph

mst, total_weight = kruskal(graph, V)

# Display the MST
print("\nEdges in the MST:")
for edge in mst:
    print(f"src: {edge.src}, dest: {edge.dest}, wt: {edge.weight}")

print(f"Minimum weight of MST: {total_weight}")

# Visualize the graph and the MST
visualize_graph(graph, mst, V)

OUTPUT:
Enter the number of edges: 4
Enter the number of vertices: 5
Enter edges in the format: src dest weight
0 1 1
0 2 1
1 3 2
2 4 2

Edges in the MST:
src: 0, dest: 1, wt: 1
src: 0, dest: 2, wt: 1
src: 1, dest: 3, wt: 2
src: 2, dest: 4, wt: 2
Minimum weight of MST: 6
