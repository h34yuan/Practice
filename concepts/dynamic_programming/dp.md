# Dynamic Programming
Dynamic Programming is an algorithmic paradigm that solves a given complex problem by breaking it into subproblems and 
stores the results of subproblems to avoid computing the same results again.
For recursive solutions with repeated calls of the same inputs, we can optimize it using dp.
Using dp reduces time complexities from exponential to polynomial. 

The two ways to store the values is bottom up (tabulation) and top down (memoization). 
For the top down approach, it starts from the top level and recursively divides the problem into sub problems until the
smallest sub problem that can be solved trivially is reached. The higher level problem obtains the optimal solution from
its sub problems. The bottom up approach does not have the recursive problem. It starts from the smallest sub problem and 
provides the result up to the higher level problem.

## Dp problem properties:
- Overlapping subproblems: Dp is only useful when that are common overlapping subproblems as there is no point storing
solutions if they are not needed again.
- Optimal substructure: a problem has optimal substructure property if the optimal solution of the gien problem can be obtained by 
using optimal solutions of its subproblems.

## Patterns:
[Minimum (Maximum) Path to reach Target](#minimum-maximum-path-to-reach-target) \
[Distinct Ways](#distinct-ways) \
[Merge Intervals](#merging-intervals) \
[Dp on Strings](#dp-on-strings) \
[Decision Making](#decision-making)

## Minimum (Maximum) Path to reach Target
Problem: Given a target, find the min/max cost/path/sum to reach the target \
Approach: Choose the min/max path among all possible paths before the current state and add it to the current state

### Template:
```pydocstring
# Generate the optimal solutions for each value in target by checking all possible
# ways and keeping the optimal one and return the value for the target.
def min_max_path_template(nums, target):
    dp = [target] * (target+1)
    for i in range(target+1):
        for j in range(len(nums)):
            if nums[j] <= i:
                dp[i] = min(dp[i], dp[i-nums[j]] + cost/path/sum)
    return dp[target]
```
### Questions:
```
120. Triangle
1043. Partition Array for Maximum Sum
646. Maximum Length of Pair Chain
322. Coin Change
518. Coin Change 2
983. Minimum Cost For Tickets
650. 2 Keys Keyboard
674. Longest Continuous Increasing Subsequence
746. Min Cost Climbing Stairs

# kadane algorithm
918. Maximum Sum Circular Subarray
53. Maximum Subarray

# 2d dp matrix
718. Maximum Length of Repeated Subarray
787. Cheapest Flights Within K Stops
1035. Uncrossed Lines
64. Minimum Path Sum
221. Maximal Square
85. Maximal Rectangle
931. Minimum Falling Path Sum
1277. Count Square Submatrices with All Ones

# store with dict
1027. Longest Arithmetic Subsequence
873. Length of Longest Fibonacci Subsequence
368. Largest Divisible Subset
467. Unique Substrings in Wraparound String
```


## Distinct Ways
Problem: Given a target, find the number of distinct ways to reach the target \
Approach: Sum all possible ways to reach the current state

### Template:
```pydocstring
# Find the optimal sum for each value in target by summing all possible ways to reach 
# the current state and return the value for the target
def distinct_ways_template(ways, target):
    dp = [0] * (target+1)
    for i in range(1, target+1):
        for j in range(len(ways)):
            if ways[j] <= i:
                dp[i] += dp[i-ways[j]]
    return dp[target]
```
### Questions:
```
300. Longest Increasing Subsequence
91. Decode Ways [can also be in string?]
377. Combination Sum IV
1109. Corporate Flight Bookings
673. Number of Longest Increasing Subsequence

2d matrix
62. Unique Paths
63. Unique Paths II

# update old dp with new dp
688. Knight Probability in Chessboard
494. Target Sum
1155. Number of Dice Rolls With Target Sum
801. Minimum Swaps To Make Sequences Increasing

# store boolean
204. Count Primes
416. Partition Equal Subset Sum

# constant dp
70. Climbing Stairs
357. Count Numbers with Unique Digits
940. Distinct Subsequences II
```

## Merging intervals
Problem: Given a set of numbers, find an optimal solution for a problem considering the current
position and the optimal value that can be retrieved from the left and right sides. \
Approach: Find all optimal solutions for every interval and return the best possible solution
 
 ### Template:
```pydocstring
# Get the best from the left and right sides and add the solution to the current position
# start from the smallest interval d and do a bottom up approach. i, j represents the left and right bound of interval d.
# Between the interval i,j we iterate k within the bounds and get the optimal solutions at k by checking the left right positions
# at k and adding the 0 to k-1 and k+1 to n intervals
def merging_interval_template(nums):
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for d in range(2, n):
        for i in range(n-d):
            j = i+d
            dp[i][j] = max(dp[i][k] + dp[k][j] + nums[k] for k in range(i+1, j))
    return dp[0][n-1]
```

### Questions:
```
1039. Minimum Score Triangulation of Polygon
312. Burst Balloons
96. Unique Binary Search Trees

# dp minimax, keep track of left and right bound indices i, j
486. Predict the Winner
877. Stone Game
```

## Dp on Strings
Problem: Given two strings s1 and s2 and return some result. 
Given one string and return some substring result \
Approach: Most problems for this pattern requires a solution that can be accepted in O(n^2) complexity.
for each position in s1, iterate all the positions in s2.

### Template:
```pydocstring
def two_string_template(s1, s2):
    m, n = len(s1) ,len(s2)
    dp = [[0] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if s1[i-1] == s2[i-1]:
                dp[i][j] = #...
            else:
                dp[i][j] = #...

def one_string_template(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for d in range(1, n):
        for i in range(n-d):
            j = i + d    
            if s[i] == s[j]:
                dp[i][j] = #...
            else:
                dp[i][j] = #...
```

### Questions:
```
# two string
516. Longest Palindromic Subsequence
712. Minimum ASCII Delete Sum for Two Strings
1143. Longest Common Subsequence
583. Delete Operation for Two Strings

# one string
647. Palindromic Substrings
139. Word Break
```

## Decision Making
Problem: Given a set of values, find the solution with an option to choose or ignore the current value. \
Approach: If chosen current value, use the previous result where the value was ignored; vice-versa,
If you decide to ignore the current value, use the previous result where the value was used.

### Template:
```pydocstring
# i - indexing a set of values, j - options to ignore j values
for i in range(n):
    for j in range(k+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j] + nums[i], dp[i-1][j-1]) # no change, cur + last valid ,last chosen
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + nums[i], nums[i]) # ignore, last chosen + cur, cur
```

### Questions:
```
2 dp keep track of count
1186. Maximum Subarray Sum with One Deletion
1567. Maximum Length of Subarray With Positive Product

constant dp
121. Best Time to Buy and Sell Stock
122. Best Time to Buy and Sell Stock II
123. Best Time to Buy and Sell Stock III
309. Best Time to Buy and Sell Stock with Cooldown
714. Best Time to Buy and Sell Stock with Transaction Fee
198. House Robber
714. Best Time to Buy and Sell Stock with Transaction Fee
213. House Robber II
1262. Greatest Sum Divisible by Three
264. Ugly Number II
740. Delete and Earn
```