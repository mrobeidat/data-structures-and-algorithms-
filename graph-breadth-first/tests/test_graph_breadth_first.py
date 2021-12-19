
from graph_breadth_first import __version__
from graph_breadth_first import *
import pytest

#@pytest
def test_version():
    assert __version__ == '0.1.0'

#@pytest
def test_add_node(value):
    node = Vertex(value)
    actual = value
    excepted = node
    assert actual == excepted

#@pytest
def test_add_edge(vertex1, vertex2, weight=1):
    edge = Edge(vertex2, weight)
    actual = weight(vertex1, vertex2)
    excepted = edge
    assert actual == excepted

#@pytest
def test_get_nodes(self):
    actual = self.graph.keys()
    excepted = actual
    assert actual == excepted

#@pytest
def test_get_neighbors():
    collection = []
    holder = {}
    actual = collection.append(holder)
    excepted = collection
    assert actual == excepted

#@pytest
def test_size(self):
    actual = len(self.graph) if len(self.graph) > 0 else None
    excepted = actual
    assert actual == excepted

#@pytest
def test_breadth_first(self, vertex):
    nodes = []
    holder = set()
    breadth = Queue()
    actual = holder.add(vertex.value), breadth.enqueue(vertex)
    excepted = nodes
    assert actual == excepted

