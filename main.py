def single_destination_shortest_path(graph, end_node):
    """
    Finds the shortest path from an end node to all other nodes in the graph.

    Args:
        graph (dict): A dictionary representing the graph structure, where keys are nodes
                      and values are lists of neighboring nodes.
        end_node: The node from which the shortest paths are calculated.

    Returns:
        dict: A dictionary containing the shortest path distances from the end node to all other nodes.
              The keys are the destination nodes, and the values are the corresponding shortest path distances.
    """
    # Implementation of the shortest path algorithm here
    pass

if __name__ == '__main__':
    # Example usage
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }
    start_node = 'A'
    end_node = 'E'
    shortest_paths = single_destination_shortest_path(graph, end_node)
    print(shortest_paths)
