# Heap
A heap is a tree based data structure in which the tree is a complete binary tree.
There are two types of heaps, max heap and min heap. For max/min heaps, the key at the root node
must be greater/smaller than all of it's children. The same property is recursively true for all sub trees.  

## Patterns to look for:
- ask for the kth smallest or largest
- Greedy, need to get the largest/smallest values each time (set of elements may also be changing)

## Greedy
use a heap to get the smallest or largest required element each time
until all the elements are visited or until condition is met

### Greedy heap template:
```pydocstring
improt heapq
# min heap sample (if max heap, change all elements to negative)
def heap_greedy_template(nums):
    heapq.heapify(nums)
    # ...
    while nums:
        # ...
        heapq.heappop()
        # ...
        # heapq.heappush(nums, ...) 
    # ...
``` 
### Greedy heap questions
```
1046. Last Stone Weight
912. Sort an Array
1508. Range Sum of Sorted Subarray Sums
1005. Maximize Sum Of Array After K Negations
1353. Maximum Number of Events That Can Be Attended
1338. Reduce Array Size to The Half
1405. Longest Happy String
```

## top k elements
Question asks to get the k-th element from some set of values
Algorithm is similar to the template above but we only heappop()
k times

```
1481. Least Number of Unique Integers after K Removals
378. Kth Smallest Element in a Sorted Matrix
347. Top k Frequent elements
973. K Closest Points to Origin
692. Top K Frequent Words
```

## Other questions:
TODO: add more details later
```
# Dijkstra
787. Cheapest Flights Within K Stops

# k-way merge
23. Merge k Sorted Lists

# two heap
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
```
