# bottom up approach: solve the simplest case and build off it
# top down approach: divide the problem for case N into sub problems (visualize a tree)
# half and half approach: eg. merge sort. sort each half of the array and then merge together the sorted halves
import List
import timeit

def fib(n):
    first = 0
    second = 1
    if n == 0 or n == 1:
        return n
    for i in range(1, n):
        temp = second
        second += first
        first = temp
    return second


def fib2(n):
    if n == 0 or n ==1:
        return n
    memo = [0] * n
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1] + memo[n-2]


# bottom up iteration. checks all smallest intervals first then increase interval size until max
def iteration_by_interval(n):
    # d is the interval sizes from min to max n
    for d in range(2, n):
        for i in range(n-d):
            j = i + d
            print(i, j)


# bottom up and top down examples for q 1039. Minimum Score Triangulation of Polygon

# bottom up starts with the smallest cases (triangles of size 3) and builds up until the entire set
def bottom_up_1039(A):
    n = len(A)
    dp = [[0] * n for _ in range(n)]
    for d in range(2, n):
        for i in range(n - d):
            j = i + d
            dp[i][j] = min(dp[i][k] + dp[k][j] + A[i] * A[j] * A[k] for k in range(i + 1, j))
    print(dp)
    return dp[0][-1]


# top down starts from the largest set (i=0, j = len(A) -1) and recursively goes until the smallest subset is solved
# and passes the values back up
def top_down_1039(A):
    memo = {}

    def top_down(i, j):
        if (i, j) not in memo:
            memo[i, j] = min([top_down(i, k) + top_down(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j)] or [0])
        return memo[i, j]
    return top_down(0, len(A) - 1)


# range sum example
def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    res = [[0] * n for _ in range(m)]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + mat[i][j]

    for i in range(m):
        for j in range(n):
            r1, c1, r2, c2 = max(0, i - K), max(0, j - K), min(m, i + K + 1), min(n, j + K + 1)
            print(i, j, dp[r2][c2], dp[r1][c1], dp[r2][c1], dp[r1][c2])
            res[i][j] = dp[r2][c2] + dp[r1][c1] - dp[r2][c1] - dp[r1][c2]
    return res


# dp questions
dp = [53, 91, 96, 139, 140, 312, 377, 413, 416, 486, 516, 583, 646, 650, 673, 688, 712, 801, 873, 877, 978, 983, 1027, 1039, 1043, 1143, 1155, 1314]


if __name__ == '__main__':
    start = timeit.default_timer()
    print(fib(5))
    stop1 = timeit.default_timer()
    print(fib2(5))
    stop2 = timeit.default_timer()
    print(stop1 - start)
    print(stop2 - start)