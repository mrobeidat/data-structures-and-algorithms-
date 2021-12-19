from collections import deque

class Vertex:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, value):
        node = Vertex(value)
        self.graph[node] = []
        return node

    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self.graph:
            raise KeyError('Vertex1 is not in the graph')

        if vertex2 not in self.graph:
            raise KeyError('Vertex2 is not in the graph')


        edge = Edge(vertex2, weight)
        self.graph[vertex1].append(edge)

    def get_nodes(self):
        return self.graph.keys()

    def get_neighbors(self, vertex):
        collection = []
        connections =  self.graph.get(vertex, [])

        for neighbor in connections:
            holder = {}
            holder[neighbor] = neighbor.weight
            collection.append(holder)

        return collection

    def size(self):
        return len(self.graph) if len(self.graph) > 0 else None

    def breadth_first(self, vertex):
        nodes = []
        holder = set()
        breadth = Queue()
        holder.add(vertex.value)
        breadth.enqueue(vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            nodes.append(front.value)

            for child in self.graph[front]:
                if child.vertex.value not in holder:
                    holder.add(child.vertex.value)
                    breadth.enqueue(child.vertex)

        return nodes