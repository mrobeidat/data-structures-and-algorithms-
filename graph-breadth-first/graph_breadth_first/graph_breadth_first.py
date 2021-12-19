from collections import deque


class Vertex:

  def __init__(self, value):

    self.value = value

class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

class Stack:
  def __init__(self):
    
    self.dq = deque()

  def push(self, value):
  
    self.dq.append(value)

  def pop(self):
  
    self.dq.pop()

class Edge:

  def __init__(self, vertex, weight):
    self.vertex = vertex
    self.weight = weight

class Graph:
    def __init__(self):
  
        self.__adjacency_list = {}

    def add_node(self, value):
      
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
       
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
       
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self.__adjacency_list.get(vertex, [])

    def breadth_first(self, start_vertex):
        queue = Queue()
        visited = set()
        final_result = ''
        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while queue.peek():
            current_vertex = queue.dequeue()
            final_result += f"{current_vertex.value} ,"
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor =  edge.vertex

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)

        return final_result


graph = Graph()

apple = graph.add_node('apple')
cherry = graph.add_node('cherry')
orange = graph.add_node('orange')
banana = graph.add_node('banana')

graph.add_edge(apple,banana)
graph.add_edge(orange,banana)
graph.add_edge(cherry,orange)
graph.add_edge(banana,cherry)

print(graph.breadth_first(apple))