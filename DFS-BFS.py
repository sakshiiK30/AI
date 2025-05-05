import matplotlib.pyplot as plt
import networkx as nx

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

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
    G = nx.DiGraph()  # Use nx.Graph() for undirected
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="skyblue",
            node_size=1200, edge_color="gray", arrows=True)
    plt.title("Graph Visualization")
    plt.show()

def main():
    graph = {}
    visited_dfs = set()
    visited_bfs = set()
    queue = []

    n = int(input("Enter number of nodes: "))
    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        graph[i] = []
        for j in range(1, edges + 1):
            node = int(input(f"Enter edge {j} for node {i}: "))
            graph[i].append(node)

    while True:
        print("\nChoose an option:")
        print("1. Perform DFS")
        print("2. Perform BFS")
        print("3. Visualize Graph")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            visited_dfs.clear()
            start_node = int(input("Enter starting node for DFS: "))
            print("The following is DFS:")
            dfs(visited_dfs, graph, start_node)
            print()
        elif choice == '2':
            visited_bfs.clear()
            queue.clear()
            start_node = int(input("Enter starting node for BFS: "))
            print("The following is BFS:")
            bfs(visited_bfs, graph, start_node, queue)
            print()
        elif choice == '3':
            print("Displaying graph...")
            visualize_graph(graph)  # This pauses until the window is closed
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
