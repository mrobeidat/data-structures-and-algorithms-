# Challenge Summary

* depth first
* Arguments: Node (Starting point of search)
* Return: A collection of nodes in their pre-order depth-first traversal order
* Display the collection


## Whiteboard Process

![Whiteboard Process]()

## Approach & Efficiency

### What approach did you take?

*Algorithm.*

### Why?

*Because : It is Graph.*

### What is the Big O space/time for this approach?

*Time : O(n) : Because : Based on the number of nodes inside the graph.*

*Space : O(1) : Because : No need for additional spaces.*

## Solution
    ```
       def depth_first(self ,start_vertex):
        list_of_items = []
        list_of_items.append(start_vertex.value)

        def walk(vertex):
            edge =self.__adjacency_list[vertex]
            for v in edge:
                my_vertex = v.vertex.value
                if my_vertex not in list_of_items:
                    list_of_items.append(my_vertex)
                    walk(v.vertex)
        walk(start_vertex)
        return list_of_items
    ```
| Subject     | links |
| ----------- | ----------- |
| graph_depth_first| [graph_depth_first/graph_depth_first.py](graph_depth_first/graph_depth_first.py) |
| test_graph_depth_first | [tests/test_graph_depth_first.py](tests/test_graph_depth_first.py) |