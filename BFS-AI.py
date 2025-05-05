import matplotlib.pyplot as plt
import networkx as nx

def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def visualize_graph(graph):
    G = nx.DiGraph()
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue",
            node_size=1200, edge_color="gray", arrows=True)
    plt.title("BFS Graph Visualization")
    plt.show()

def main():
    graph = {}
    visited = set()
    queue = []

    n = int(input("Enter number of nodes: "))
    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        graph[i] = []
        for j in range(1, edges + 1):
            node = int(input(f"Enter edge {j} for node {i}: "))
            graph[i].append(node)

    start_node = int(input("Enter starting node for BFS: "))
    print("BFS Traversal:")
    bfs(visited, graph, start_node, queue)
    print()

    visualize_graph(graph)

if __name__ == "__main__":
    main()

OUTPUT:
Enter number of nodes: 4
Enter number of edges for node 1: 2
Enter edge 1 for node 1: 2
Enter edge 2 for node 1: 3
Enter number of edges for node 2: 1
Enter edge 1 for node 2: 4
Enter number of edges for node 3: 1
Enter edge 1 for node 3: 4
Enter number of edges for node 4: 0
Enter starting node for BFS: 1
BFS Traversal:
1 2 3 4
