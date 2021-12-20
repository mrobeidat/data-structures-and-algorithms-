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

def business_trip(graph, city_names):

    global cost
    global can1
    global can2

    status = True
    cost = 0
    can1 = 0
    can2 = 1

    def trip(graph, start, end):

        path = graph.graph[start]

        for city in path:
            if end == city.vertex:
                global cost
                cost += city.weight

                if end.value == city_names[-1].value:
                    break
                else:
                    global can1
                    can1 += 1
                    global can2
                    can2 += 1
                    trip(graph, city_names[can1], city_names[can2])

    trip(graph, city_names[can1], city_names[can2])

    if cost == 0:
        status = False

    cost = f"${str(cost)}"
    return (status, cost,)

if __name__ == '__main__':

    graph = Graph()

    pandora = graph.add_node('pandora')
    arendelle = graph.add_node('arendelle')
    metroville = graph.add_node('metroville')
    narina = graph.add_node('narina')
    naboo = graph.add_node('naboo')
    manstropolis = graph.add_node('manstropolis')

    graph.add_edge(pandora,arendelle,150)
    graph.add_edge(pandora,metroville,82)
    graph.add_edge(arendelle,pandora,150)
    graph.add_edge(arendelle,metroville,99)
    graph.add_edge(arendelle,manstropolis,42)
    graph.add_edge(metroville,pandora,82)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(metroville,manstropolis,105)
    graph.add_edge(metroville,naboo,26)
    graph.add_edge(metroville,narina,37)
    graph.add_edge(narina,metroville,37)
    graph.add_edge(narina,naboo,250)
    graph.add_edge(naboo,narina,250)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(naboo,manstropolis,73)
    graph.add_edge(manstropolis,naboo,73)
    graph.add_edge(manstropolis,arendelle,42)
    graph.add_edge(manstropolis,metroville,105)
    
    print()
    print(business_trip(graph,[pandora,arendelle]))
    print()