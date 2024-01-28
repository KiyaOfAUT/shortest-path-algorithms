import heapq


class Graph:
    def __init__(self, v: int):
        self.V = v
        self.adj = [[] for _ in range(self.V)]

    def add_edge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))

    def print_arr(self, dist, previous, changed):
        print("Vertex || Distance from Source || previous vertex")
        for i in range(len(self.adj)):
            msg = "{0}\t\t || {1}\t\t || {2}".format(i, dist[i], previous[i])
            if changed == i:
                msg = msg + "  changed!! "
            print(msg)

    def dijkstra(self, src: int):
        for v in self.adj:
            for u, w in v:
                if w < 0:
                    print("can not use dijkstra on graphs with negative weight!")
                    return
        counter = 1
        pq = []
        previous = [-1] * len(self.adj)
        heapq.heappush(pq, (0, src))
        dist = [float("inf")] * self.V
        checked = [0] * self.V
        dist[src] = 0
        print("initial:")
        self.print_arr(dist, previous, -1)
        while pq:
            d, u = heapq.heappop(pq)
            for v, weight in self.adj[u]:
                if dist[v] > dist[u] + weight and checked[v] == 0:
                    print("\nstep:  ", counter)
                    previous[v] = u
                    counter += 1
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
                    self.print_arr(dist, previous, v)
            checked[u] = 1
        print("\nfinal result:")
        self.print_arr(dist, previous, -1)

    def bellman_ford(self, src, print_=1):
        dist = [float("Inf")] * len(self.adj)
        dist[src] = 0
        previous = [-1] * len(self.adj)
        if print_:
            print("initial:")
            self.print_arr(dist, previous, -1)
        for _ in range(len(self.adj) - 1):
            for u in range(len(self.adj)):
                for v, w in self.adj[u]:
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        previous[v] = u
                        dist[v] = dist[u] + w
                        if print_:
                            self.print_arr(dist, previous, v)
        for u in range(len(self.adj)):
            for v, w in self.adj[u]:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    print("Graph contains negative weight cycle")
                    return -1
        if print_:
            print("\nfinal result:")
            self.print_arr(dist, previous, -1)
        return dist

    def johnson(self):
        new_edge = len(self.adj)
        self.adj.append([])
        for i in range(new_edge):
            self.add_edge(new_edge, i, 0)
        bellman_ford_dist = self.bellman_ford(new_edge, 0)
        if bellman_ford_dist == -1:
            return
        print("distance between the virtual node and other nodes: ", bellman_ford_dist[:new_edge])
        for u in range(new_edge):
            for i in range(len(self.adj[u])):
                self.adj[u][i] = (self.adj[u][i][0], self.adj[u][i][1] + bellman_ford_dist[u] - bellman_ford_dist[self.adj[u][i][0]])
        self.adj.pop()
        print(" all edges after johnson algorithm: ", self.adj)
