from collections import Counter, defaultdict
import heapq
from random import randrange

# presum and sliding window to find subarrays with sum S
def numSubarraysWithSum(self, A, S) -> int:
    c = Counter({0: 1})
    psum = res = 0
    for i in A:
        psum += i
        res += c[psum - S]
        c[psum] += 1
    return res

# int to binary string
def int_to_bin(s):
    # {} place a variable into a string
    # 0 takes variable at arg pos 0
    # : adds formatting option
    # 0n formats num to n digit zero padding on left
    # b converts to binary representation
    return"{0:b}".format(s)


# Dijkstra's algorithm with heapq
# and input edges is list of tuples with (start, end, cost)
def dijkstra(edges, start, end):
    paths = defaultdict(dict)
    for s, e, cost in edges:
        paths[s][e] = cost
    # print(paths)
    # q contains tuples of cost, v1 node, path
    # seen is set of visited nodes,
    # mins is the min cost to each node from start
    q, seen, mins = [(0, start, [])], set(), {start: 0}
    while q:
        cost, v1, path = heapq.heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = path + [v1]
            if v1 == end:
                return cost, path

            # bfs for cur node
            for v2 in paths[v1]:
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                print(prev, path, v2)
                next = paths[v1][v2] + cost
                if prev is None or next < prev:
                    mins[v2] = next
                    heapq.heappush(q, (next, v2, path))
    return float('-inf')


# Implement randM() using randN() when M > N:
# Step 1: Use randN() to generate randX(), where X >= M. In this problem, I use 7 * (rand7() - 1) + (rand7() - 1) to generate rand49() - 1.
# Step 2: Use randX() to generate randM(). In this problem, I use rand49() to generate rand40() then generate rand10.
# N^b * (randN() - 1) + N^(b - 1) * (randN() - 1) + N^(b - 2) * (randN() - 1) + ... + N^0 * (randN() - 1) generates randX() - 1, where X = N^(b + 1)
def rand7():
    return randrange(1, 8)

def rand10(self):
    """
    :rtype: int
    """
    res = 40
    while res >= 40:
        res = 7 * (rand7() - 1) + (rand7() - 1)
    return res % 10 + 1


if __name__ == '__main__':
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]
    print(dijkstra(edges, "A", "E"))
