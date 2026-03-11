# Dijkstra's Algorithm

## Problem
We need to find the shortest path distances from the source vertex to all other vertices in the graph.
The input is a weighted undirected graph and a source vertex `(src)`. 

## Greedy Idea
This is done by maintaining a set of explored nodes S for which we have determined the shortest path distance `d(u)` from `s` to `u`.
Then Initialize `S = { s }`, `d(s) = 0`.
Repeatedly choose unexplored node v which minimizes distance. Add `v` to `S`, and set `d(v) = π(v)`.
This algorithm requires all weights not be negative.

## Pseudocode
```text
    Dijkstra (Graph G, Node src)
	for each vertex v in V
		D[v] = G.weight(s, v) // ∞ for unreachable
	S = {s}
	while (V – S is not empty)
		u = Cheapest vertex reachable from V – S 
		S.add(u)
        # edge relaxation
		for each vertex v adjacent to u
			if (D[v] > D[u] + G.weight(u, v))
				D[v] = D[u] + G.weight(u,v)
```

## Implementation & Time Cmplexity
The time complexity is `O((V+E)*logV)`, Where `E` is the number of edges and `V` is the number of vertices.
A **min-heap** is used for implementation. 

### The example graph
```
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
```

### Corresponding Adjacency List:
- 0 → (1,4), (2,8)
- 1 → (0,4), (4,6), (2,3)
- 2 → (0,8), (3,2), (1,3)
- 3 → (2,2), (4,10)
- 4 → (1,6), (3,10)

#### Min-Heap implementation details
A min-heap is a *complete* binary tree (all levels are filled, except the bottom one, which fills in from the left). 
Children of nodes in the tree are always larger than their parent nodes. The smallest node is always the root node.
Python implements min-heaps using an underlying array. The smallest node is always at index `0`.
Finding a node in a min-heap array can be done in this way:
 If a node is stored at index i:
 - Its left child is at index `2*i + 1`.
 - Its right child is at index `2*i + 2`.
 - The parent of a node at index i can be found at index `[(i-1)/2]`.
