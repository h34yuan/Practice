import random
import numpy as np


def random_adjacency_matrix(n):
    """
    creates an nxn symmetric adjacency matrix with 0s along the diagonal
    used to represent an undirected graph with n nodes
    :param n: dimension
    :return: nxn numpy array
    """
    matrix = [[random.randint(0, 1) for i in range(n)] for j in range(n)]

    # No vertex connects to itself
    for i in range(n):
        matrix[i][i] = 0

    # If i is connected to j, j is connected to i
    for i in range(n):
        for j in range(n):
            matrix[j][i] = matrix[i][j]

    return np.array(matrix)


# dfs of adjacency matrix
def dfs(matrix, start, visited: dict):
    print(start)
    visited[start] = True
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and i not in visited:
            dfs(matrix, i, visited)


def bfs(matrix, start=0):
    visited = {}
    q = [start]
    visited[start] = True

    while len(q) > 0:
        curr = q.pop(0)
        print(curr)
        for i in range(len(matrix[curr])):
            if matrix[curr][i] == 1 and i not in visited:
                visited[i] = True
                q.append(i)


# topological dfs
def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]
    # create graph
    for pair in prerequisites:
        x, y = pair
        graph[x].append(y)
    # visit each node
    for i in range(numCourses):
        if not self.dfs(graph, visited, i):
            return False
    return True


def dfs_topological(self, graph, visited, i):
    # if ith node is marked as being visited, then a cycle is found
    if visited[i] == -1:
        return False
    # if it is done visted, then do not visit again
    if visited[i] == 1:
        return True
    # mark as being visited
    visited[i] = -1
    # visit all the neighbours
    for j in graph[i]:
        if not self.dfs(graph, visited, j):
            return False
    # after visit all the neighbours, mark it as done visited
    visited[i] = 1
    return True


# keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.
# finds any overlapping connections in the undirected graph and returns the redundant edge in order to form tree
def union_find_overlap(edges):

    parent = [0] * len(edges)

    # determine which subset the element x belongs to
    def find(x):
        if x != 0:
            parent[x] = find(parent[x])
        return parent[x]
        # if parent[x] == 0:
        #     return x
        # return find(parent[x])

    # # iterative find
    # def find(x):
    #     while x != parent[x]:
    #         parent[x] = parent[parent[x]]
    #         x = parent[x]
    #     return x

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

    for x, y in edges:
        if not union(parent, x - 1, y - 1):
            return [x, y]


if __name__ == '__main__':
    matrix = [[0, 1, 0, 0, 1, 1],
              [0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]
    # dfs(matrix, 0, {})
    bfs(matrix, 0)