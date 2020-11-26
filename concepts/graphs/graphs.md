# Graphs
A graph consists of a finite set of nodes and a set of edges connecting the nodes.
Read [10-graph-algorithms-visually-explained](https://towardsdatascience.com/10-graph-algorithms-visually-explained-e57faa1336f3)
for a more detail explanation of definitions and algorithms

TODO: move the grid problems to here

## Patterns to look for:
- input is a list of edges, adjacency list, matrix or grid.
- question asks for the traversal of paths or shortest/longest path
- question asks to find groupings or components 

## Dfs topological sort graph
This subset of problems involves the use of dfs to find the topological sorting of the vertices.
Topological sorting is a linear sorting of vertices such that for every directed edge
u v, from vertex u to v, u comes before v in ordering. This can only be applied on directed acyclic graphs (DAG) 
The first vertex in the ordering is always a vertex with in-degree as 0 (no incoming edges). 

Common patterns of topological sort problems involve the question asking to start at a specific 
vertex and find all the paths to some target vertex.

### Topological sort template
```pydocstring
def topological_sort_template(graph: List[List[int]]):
    # initialize other data structures if necessary
    # ...
    res = []
    def dfs(i):
        # ... 
        for x in graph[i]: # iterate all neighbours of i
            # ...
            dfs(x)
        res.append(i)
    dfs(0) # start at some vertex or iterate all vertices
    # for i in range(len(graph):
    #   dfs(i)
    return res
```         

### Topological sort Questions:
```
207. Course Schedule
332. Reconstruct Itinerary
797. All Paths from source target
```

# Graph bfs
For this subset of problems, we iterate all the children nodes of the current node
before moving on to the vertices in the next level. Graphs can contain cycles
as we may have to keep track of the visited vertices for some problems.

```
997. Find the Town Judge
1615. Maximal Network Rank
```

## Union find
For problems with an edge list as input and asks for the number of connected components,
union find is used. Union find is a data structure that keeps track of a set of 
elements partitioned into a number of disjoint (non-overlapping) subsets.

The two operations is find which determines which subset an element belongs to
and union which joins two subset into a single subset.

### Union find template
```pydocstring
def union_find_template(edges):
    parents [0] * len(edges)
    
    # determine which subset the element x belongs to
    def find(x):
        if x != 0:
            parent[x] = find(parent[x])
        return parent[x]
    
    # joins two subsets into single subset
    def union(parent, x, y):
        x_set = find(x)
        y_set = find(y)
        # if two nodes result in the same subset (same connected component) edge is redundant as subsets of x and y
        # the same
        if x_set == y_set:
            return False
        parent[x_set] = y_set
        return True
    
    # iterate edges
    for x,y in edges:
        # do something based on the question
        # ...
        # this example finds redundant connections that can be removed to form a tree
        if not union(parent, x-1, y-1):
                return [x, y]
```

### Union find questions:
```
684. Redundant Connection
547. Friend Circles
990. Satisfiability of Equality Equations
721. Accounts Merge
1202. Smallest String With Swaps
```

## Other questions:

### Bellman-Bord and Dijkstra's algorithm
TODO: find more questions
used to find shortest path from one vertex to another
```
1514. Path with Maximum Probability

```

### set operation
```
1557. Minimum Number of Vertices to Reach All Nodes
```
