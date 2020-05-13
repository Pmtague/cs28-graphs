from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = Graph()

    for member in ancestors:
        ancestor_graph.add_vertex()
        ancestor_graph.add_edge(member[1], member[0])