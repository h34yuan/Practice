# bottom up approach: solve the simplest case and build off it
# top down approach: divide the problem for case N into sub problems (visualize a tree)
# half and half approach: eg. merge sort. sort each half of the array and then merge together the sorted halves

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


if __name__ == '__main__':
    start = timeit.default_timer()
    print(fib(5))
    stop1 = timeit.default_timer()
    print(fib2(5))
    stop2 = timeit.default_timer()
    print(stop1 - start)
    print(stop2 - start)