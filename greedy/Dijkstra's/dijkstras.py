# Python's min-heap class 
import heapq

"""
This function returns an array of shortest path distances from the source node to all other nodes.
Inputs: the adjacency list that represents the graph, and a source node.
"""
def dijkstra(adj, src):
    V = len(adj)                                    # V is the number of vertices in the graph
    dist = [float('inf')] * V                       # The distances array is filled up with ∞ at the start
    dist[src] = 0                                   # Start with the source, the distance to itself is 0

    # priority queue (min-heap) - smallest distance is always at index 0
    pq = [(0, src)]                                 # (distance, node)

    # continue until all reachable nodes are processed
    while pq:
        d, u = heapq.heappop(pq)                    # select and remove the node with the smallest current distance 

        if d > dist[u]:                             # if the distance found is larger than a better case, ignore it
            continue
        
        for v, w in adj[u]:                         # looking through neighbors (vertices + weights)
            if dist[u] + w < dist[v]:               # check if the path through u gives a smaller distance than the current dist[v]
                dist[v] = dist[u] + w               # update the distance
                heapq.heappush(pq, (dist[v], v))    # update the priority queue
    return dist

# source node
src = 0
# adjacency list
adj = [
    [(1, 4), (2, 8)],
    [(0, 4), (4, 6), (2, 3)],
    [(0, 8), (3, 2), (1, 3)],
    [(2, 2), (4, 10)],
    [(1, 6), (3, 10)]
]

print("The graph:\n")
print(r"""
       (4)
 0 -------- 1
 | \        |
 |  \(3)    |(6)
(8)  \      |
 |    \     |
 2 ---(2)---3
      \
       \(10)
        \
         4
""")
result = dijkstra(adj, src)
print("source node: ", src, "\n")
print("Dijkstra's shortest path distances: ")
print(result) 