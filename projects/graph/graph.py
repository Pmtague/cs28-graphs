"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # Initialize dictionary to store vertices and their edges
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # Add new vertices to the dictionary with an instantiated set as the value
        self.vertices[vertex_id] = set()    # Set of edges

    # Add a directed edge to the graph (v1 to v2)
    def add_edge(self, v1, v2):

        # Check vertices dictionary for both vertices
        if v1 in self.vertices and v2 in self.vertices:
            # If both are preset, add the second vertex as the value of the first
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        # Return the value of the given vertex_id (neighbor)
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):

        #Instantiate an empty queue
        q = Queue()

        # Add the starting vertex to the queue
        q.enqueue(starting_vertex)

        # Keep track of visited nodes
        visited = set()

        # Repeat until queue is empty
        while q.size() > 0:

            # Dequeue first vertex
            v = q.dequeue()

            # If it's not visited:
            if v not in visited:
                print(v)

                # Mark visited
                visited.add(v)

                # Enqueue all unvisited neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    # Print each vertex in depth-first order beginning from starting_vertex.
    def dft(self, starting_vertex):

        # Instantiate an empty stack
        s = Stack()

        # Add the starting node to the stack
        s.push(starting_vertex)

        # Keep track of visited nodes
        visited = set()

        # Repeat until stack is empty
        while s.size() > 0:

            # Pop first vertex
            v = s.pop()

            # If it's not visited:
            if v not in visited:
                print(v)

                # Mark visited
                visited.add(v)

                # Push all unvisited neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    # Print each vertex in depth-first order beginning from starting_vertex.

    def dft_recursive(self, starting_vertex, visited = None):
        
        # Initialize an empty set for visited vertices
        if visited is None:
            visited = set()
        
        # Add the starting vertex to visited
        visited.add(starting_vertex)
        print(starting_vertex)

        # Skip using a stack and loop through the neighbors
        for next_vert in self.get_neighbors(starting_vertex):

            # If the neighbor hasn't been visited
            if next_vert not in visited:

                # Run the entire function on the next_vert
                self.dft_recursive(next_vert, visited)

    # Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order.
    def bfs(self, starting_vertex, destination_vertex):
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Vertices", graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
