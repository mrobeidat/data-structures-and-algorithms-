from graph_depth_first import __version__
from graph_depth_first.graph_depth_first import Graph, Vertex
import pytest
def test_version():
    assert __version__ == '0.1.0'



def test_depth_first():
    graph = Graph()

    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h = graph.add_node('H')

    graph.add_edge(a,b)
    graph.add_edge(a,d)

    graph.add_edge(b,c)
    graph.add_edge(b,d)

    graph.add_edge(c,g)

    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)

    graph.add_edge(f,h)


    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    actual = graph.depth_first(a)
    assert actual == expected