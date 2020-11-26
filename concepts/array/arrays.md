# Arrays
The algorithm question's input is in the form of an array or matrix. Questions requires the traversal of the array
to output some computation or to make modifications to the existing array based on the questions constraint.

The generic array/matrix questions can be solved in one pass linear time where each element is check at least once.

For each set of array questions, it can have properties of more than one sub pattern.

## Generic array questions

```
59. Spiral Matrix II
849. Maximize Distance to Closest Person
945. Minimum Increment to Make Array Unique
119. Pascal's Triangle II
1296. Divide Array in Sets of K Consecutive Numbers
846. Hand of Straights
1184. Distance Between Bus Stops
566. Reshape the Matrix
448. Find All Numbers Disappeared in an Array
1013. Partition Array Into Three Parts With Equal Sum
189. Rotate Array
665. Non-decreasing Array
581. Shortest Unsorted Continuous Subarray
915. Partition Array into Disjoint Intervals
334. Increasing Triplet Subsequence
905. Sort Array By Parity
442. Find All Duplicates in an Array
1299. Replace Elements with Greatest Element on Right Side
1014. Best Sightseeing Pair
1491. Average Salary Excluding the Minimum and Maximum Salary
832. Flipping an Image
1593. Split a String Into the Max Number of Unique Substrings
1582. Special Positions in a Binary Matrix
807. Max Increase to Keep City Skyline
896. Monotonic Array
1464. Maximum Product of Two Elements in an Array
1089. Duplicate Zeros
1267. Count Servers that Communicate
```

## Iterate from both ends, 2 pass
This subset of array questions requires two pass, starting at each end of the array

### Patterns to look for:
- looking for different patterns of the array from each end (increasing from both ends)
- finding some total in the array excluding the current index
```
941. Valid Mountain Array
238. Product of Array Except Self
```

## sort array with condition
This subset of array questions requires the sorting of the initial array based on some condition
before solving. 

### Patterns to look for:
- the order of the initial array is irrelevant and can be changed 
- looking for differences/overlaps between elements
```
1509. Minimum Difference Between Largest and Smallest Value in Three Moves
1200. Minimum Absolute Difference
1288. Remove Covered Intervals
406. Queue Reconstruction by Height
1233. Remove Sub-Folders from the Filesystem
1502. Can Make Arithmetic Progression From Sequence
```

## Greedy
For this subset of array questions, on each iteration, the question is solved by
always trying to get the largest/smallest val available based on the questions constraints.

### Patterns to look for:
- looking to find the min/max result or if some position can be reached based on given constraints
- question hints at greedily taking the largest/smallest next possible value
at the current index
```
# greedy
435. Non-overlapping Intervals
134. Gas Station
1029. Two City Scheduling
55. Jump Game
1094. Car Pooling
738. Monotone Increasing Digits
1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
```

### Merge Intervals:
For merge interval problems that gives a list of intervals, we will need to sort the intervals 
by the start or the end depending on the question and check for overlaps. 
(Problems can be under subset of greedy problems)
```
56. Merge Intervals
435. Non-overlapping Intervals
621. Task Scheduler [heapq]
```

## Hashmap to store values
This subset of questions iterates the array and uses a dict or set to store seen values, indices or some other constraint
 to prevent visiting already seen values (related to hashmap question set).

### Patterns to look for:
- looking for the occurrence of elements in array
- looking for matching or overlap of values/indices
```
1222. Queens That Can Attack the King
670. Maximum Swap
792. Number of Matching Subsequences
888. Fair Candy Swap
1539. Kth Missing Positive Number
1122. Relative Sort Array
1380. Lucky Numbers in a Matrix
```

## Non-tree bfs traversal
TODO move to backtrack?
Bfs pattern is applied on problems where the input can be an array of int/string or a matrix instead of a Tree.
Bfs on tree and graph structures are explained on a separate page as this subset of questions focuses
on bfs on arrays, integers, strings and matrices. 

### Patterns to look for:
- question hints at finding all the nearest surrounding values first (shortest path)
- input is a matrix and question asks for nearest or the adjacent values of the current cell
- input is an (array of or just) an integer/string and asks to modify it to some target but can only 
change a set amount of digits or characters each time.
```
542. 01 Matrix
994. Rotting Oranges
690. Employee Importance
752. Open the Lock
127. Word Ladder
967. Numbers With Same Consecutive Differences
```