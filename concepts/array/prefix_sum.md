# Prefix Sum
Prefix sum is the process of computing the cumulative total (based on some condition) so far at the current index and stores the current total and index in an array or hashmap (Stored as {tot: index} in a hashmap).
This process is typically used to find subarrays equal to some target (min/max sum/product subarray or subarray equal to target t) by taking the difference between 
two prefix totals (keys in hashmap) which represents the total of some subarray between those indices. Prefix sum is used to reduce the traversal runtime to linear and the prefix data structure is 
usually initialized with 0 total and some initial index/count for checking subarrays with a left bound of index 0.

## Patterns to look for in questions:
- questions ask to find contiguous subarrays with some subarray total condition that equals to some target
- can be asked to find the total count or the indices/ length of contiguous subarray that meets the condition 
## Code template
```pydocstring
# looking for all subarray with target 
def prefix_sum_template(nums: List[int], target: int):
    prefix = {0:1} # if looking for length, value is usually initialized to -1
    tot = 0
    # ...
    for i, x in enumerate(nums):
        tot += x 
        if prefix[tot - target]: 
            # do something if the diff between total and target exists
        prefix[tot] = prefix.get(tot) + 1  # i/setdefault(tot, i) if working with most recent/first seen index
        # ... 
```
## Questions list:

### Prefix stores the running total as the key and the index or number of occurrences as value.
```
930. Binary Subarrays With Sum
974. Subarray Sums Divisible by K
1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
523. Continuous Subarray Sum
152. Maximum Product Subarray
560. Subarray Sum Equals K
525. Contiguous Array
```
### Prefix used to find the number of elements to remove from array/list until target is met. Prefix stores the index of the last occurring tot {presum tot: last seen index}
```
1590. Make Sum Divisible by P
1171. Remove Zero Sum Consecutive Nodes from Linked List
```

```
1031. Maximum Sum of Two Non-Overlapping Subarrays
862. Shortest Subarray with Sum at Least K
```