# ShortestPathGraph
this library contains a graph class capable of solving shortest path problems.
## features:
* construct a given graph with n edges and m weighted vertices
* finds shortest path and minimum distance between given source and other vertices using dijkstra(if all edges are weighted positive) or Bellman-Ford
* makes all negative weighted edges positive by using johnson algorithm
* detects negative cycles 

## how to use:
### constructing graphs:
* to construct graph `g` with `n` vertices use:
`g = Grap(n)`
* to add `(u, v)` edge with weight of `w` use:
`g.add_edge(u, v, w)`
### shortest path:
* to calculate the shortest path from source src to other vertices by dijkstra use:
`g.dijkstra(src)`
* to calculate the shortest path from source src to other vertices by Bellman-Ford use:
`g.bellman_ford(src)`
### negative cycle detection:
* to detect negative cycles in graph `g` use:
`g.bellman_ford(0, 0)`
### all weights positive:
* to make all weights positive by johnson use:
`g.johnson()`
