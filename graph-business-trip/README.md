# Challenge Summary

* Write a function called business trip
* Arguments: graph, array of city names
* Return: cost or null

## Whiteboard Process

![Whiteboard Process]()

## Approach & Efficiency

### What approach did you take?

*Algorithm.*

### Why?

*Because : It is Graph.*

### What is the Big O space/time for this approach?

*Time : O(n) : Because : When finding the requirements it will break.*

*Space : O(1) : Because : No additional spaces.*

## Solution

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

| Subject     | links |
| ----------- | ----------- |
| graph_business_trip| [graph_business_trip/graph_business_trip.py](graph_business_trip/graph_business_trip.py) |
| test_graph_business_trip | [tests/test_graph_business_trip.py](tests/test_graph_business_trip.py) |