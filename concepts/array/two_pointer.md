# Two Pointer 
Two pointer is when two points itereate through the data structure in tandem until one or both pointer conditions is met.
It is used to find a pair or some subarray of elements based on some constraint at reduced runtime as continually looping
back with a single pointer is unnecessary.
Pointers are usually initialized at each end of the data structure but can start at any position
(For linked lists, two pointers are used for many problems such as slow fast pointers)

## Patterns to look for in questions:
- problems where the data structure is some sorted arrays, linkedlist or deals with the position indices 
and need to find some set of elements
- asked to find the pair, triplet or subarray of elements in the array (3sum, 4sum)
- problem asked to sort/reorder the input array with some constraint

## Code template
```pydocstring
def two_pointer_template(nums: List[int], cond):
    nums.sort() # sort input if necessary
    l, r = 0, len(nums) -1 # initialize pointers at each end
    # ...
    while l < r:
        if left cond: 
            l += 1
        if right cond:
            r -= 1
    # ...

# pointers used to keep track of l/r position but iterate the input from one side
def two_pointer_position_template(nums: List[int], cond):
    l, r = 0, 0 # initialize pointers at some point
    # ...
    for i in range(len(nums)):
        # ...
        if i and l cond:
            l = # ...
        if i and r cond:
            r = # ...
        # ...
```
## Questions list:

### Reorder/sort input 
```
977. Squares of a Sorted Array
922. Sort Array By Parity II
1574. Shortest Subarray to be Removed to Make Array Sorted
283. Move Zeroes
31. Next Permutation
```
### Find subsets
```
923. 3Sum With Multiplicity
167. Two Sum II - Input array is sorted
15. 3Sum
18. 4Sum
1498. Number of Subsequences That Satisfy the Given Sum Condition
881. Boats to Save People
763. Partition Labels
724. Find Pivot Index
795. Number of Subarrays with Bounded Maximum
```

### Others
```
42. Trapping Rain Water
45. Jump Game II
```
