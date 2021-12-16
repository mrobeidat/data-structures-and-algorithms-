# Graphs

***A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.***

**Here is some common terminology used when working with Graphs:**

* Vertex :

*A vertex, also called a “node”, is a data object that can have zero or more adjacent vertices.*

* Edge :

*An edge is a connection between two nodes.*

* Neighbor :

*The neighbors of a node are its adjacent nodes, i.e., are connected via an edge.*

* Degree :

*The degree of a vertex is the number of edges connected to that vertex.*

## Challenge

### Features

*Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:*

* add node

1. Arguments: value
2. Returns: The added node
3. Add a node to the graph

* add edge

1. Arguments: 2 nodes to be connected by the edge, weight (optional)
2. Returns: nothing
3. Adds a new edge between two nodes in the graph
4. If specified, assign a weight to the edge
5. Both nodes should already be in the Graph

* get nodes

1. Arguments: none
2. Returns all of the nodes in the graph as a collection (set, list, or similar)

* get neighbors

1. Arguments: node
2. Returns a collection of edges connected to the given node
3. Include the weight of the connection in the returned collection

* size

1. Arguments: none
2. Returns the total number of nodes in the graph

## Approach & Efficiency

### What approach did you take?

**Algorithm.**

### Why?

**Because : It is Graph.**

### What is the Big O space/time for this approach?

> Add Node

**Time : O(1).**

**Space : O(1).**

> Add Edge

**Time : O(n).**

**Space : O(n).**

> Get Nodes

**Time: O(n).**

**Space: O(n).**

> Get Neighbors

**Time: O(n).**

**Space: O(n).**

> Size:

**Time: O(1).**

**Space: O(1).**

## API

**add node that added new value to graph.**

**add edge that makes nodes in graph connected.**

**get nodes in the graph.**

**get neighbors.**

**size that lets you know the total number of nodes in the graph.**

| Subject     | links |
| ----------- | ----------- |
| graph| [graphs/graph.py](graphs/graph.py) |
| test_graph | [tests/test_graphs.py](tests/test_graphs.py) |