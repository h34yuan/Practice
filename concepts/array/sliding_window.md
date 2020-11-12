# Sliding Window
sliding window pattern is used to compute some operations on a specific window size in an array or linked list. Sliding window will start from one end and shift by one element on each iteration
and adjust the length of the window accordingly as the window size can be constant or dynamic.

## Patterns to look for in questions:
- input is a linear data structure(array, linked,list, string)
- finding the longest/shortest subarray (e.g. longest even subarray)
- find some size k subarrays that satisfy some condition (e.g. max sum of subarray of size k)

## Code template
```pydocstring
def sliding_window_template(input_arr: List[int], k: int):
    # initialize some other data structures to for question if needed
    window = # some calculation of the first k elements
    for i in range(k, len(input_arr)): # iterate array
        window = window + # some calculation to include ith element
        winodw = window - # some calculation to remove i-k element
        # ...

# template for changing window size 
def sliding_window_pointer_template(input_arr: List[int], k: int):
    window = # some calculation of the first k elements
    i, j =  # initialize window left and right bounds
    while i, j < # some condition
        if # move j condition:
            j += 1
        if # move i condition: 
            i += 1
        # ...
```
## Questions list:
```
424. Longest repeating character replacement
567. Permutation in string
209. Minimum size subarray sum
1493. Longest Subarray of 1's After Deleting One Element
1004. Max Consecutive Ones III
1423. Maximum Points You Can Obtain from Cards
76. Minimum Window Substring
643. Maximum Average Subarray I
1052. Grumpy Bookstore Owner
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
```

