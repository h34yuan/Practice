# Modified binary search
When the question gives a sorted array, number range or matrix and asks to find a certain element, the best algorithm to use 
is binary search. Binary search can also be applied to problems that asks for a certain element given an input of an unsorted array and
some threshold value and asks to find a certain value.   

For best practice, use mid = start + (end-start) / 2 instead of (start + end) / 2 to prevent integer overflow.

## Patterns to look for:
- input is a sorted array, linked list, matrix or an integer range and question asks to find a certain value
- input is an unsorted array and some threshold value. Question asks to find some minimum value based on the threshold.


## Sorted binary search
Binary search initializes the l/r base on given numerical values instead of index.
Input can be a sorted array, matrix or an integer.

### Sorted matrix sample code template:
```pydocstring
# Searching for a element in a sorted 2D matrix 
# sorted row wise and first int on each row is greater than last in on prev row
def search_sorted_matrix_sample(matrix, target):
    if not matrix or target is None:
            return False
        rows, cols = len(matrix), len(matrix[0])
        l, h = 0, rows * cols - 1
        while l <= h:
            mid = (l+h) // 2
            num = matrix[mid//cols][mid%cols]
            if num == target:
                return True
            elif num < target:
                l = mid+1
            else:
                h = mid-1
        return False
```

### Sorted binary search questions:
```
74. Search a 2d matrix
240. Search a 2D Matrix II
1351. Count Negative Numbers in a Sorted Matrix
278. First Bad Version
367. Valid Perfect Square
```

## Unsorted array and threshold
This subset of questions gives an array of unsorted values and some threshold target.
 
 The questions asks
to find a minimum value that gives some count or total for each subarrays or the entire array that is less than equal to the threshold 
This type of binary search initializes the low/high with 0, 1, max/ max, total depending on the problem

One each iteration of the binary search, the entire array is iterated through to calculate some value (count/total) by checking
against the mid value and then the calculated value is compared with the threshold to change the low/high

### Threshold binary search template
```pydocstring
# template is based on 410. split array largest sum
def threshold_bs_template(nums: List[int], threshold: int): 
    low, high = max(nums), sum(nums) # initialize low high. Values differ by question
    while low < high:
        mid = low + (high-low) // 2
        # set metrics used to compare with threshold
        cur, count = 0, 1 # number of vars depend on question
        for num in nums:
            # metric and mid condtion
            if cur + num > mid:
                cur = 0
                count += 1
            cur += num
        # binary search part
        if count > threshold:
            low = mid + 1
        else:
            high = mid
    return low
```

### Unsorted array and threshold questions:
```
875. Koko Eating Bananas
1011. Capacity To Ship Packages Within D Days
410. Split Array Largest Sum
1283. Find the Smallest Divisor Given a Threshold
1300. Sum of Mutated Array Closest to Target
1552. Magnetic Force Between Two Balls
```

## Other Questions:
```
# binary search of position index
1337. The K Weakest Rows in a Matrix

# binary search with bisect
1268. Search Suggestions System
```
