# Backtrack
Backtrack is a general algorithm for finding a subset to some computational problems, that incrementally builds to the solution.
 In backtracking, you stop evaluating a certain path once it breaks some constraint from the problem, 
 and takes a step back to the previous level. It will then try other possible cases and see if those will lead to a valid solution.
 
Backtracking is most commonly used for solving constraint satisfaction problems (CSPs are mathematical questions defined as a set of objects whose state must satisfy some number of constraints or limitations)
since it is a systematic generating method that avoids repetitions and completely checks all combinations and permutations.

Comparing with dfs, backtracking is a more general purpose algorithm as dfs is a specific fom of backtracking relating to trees.
Backtracking can be seen as dfs with an added constraint that we stop exploring the subtree as soon as it fails the given constraint. 
 
## patterns to look for:

- Questions asks to return a collection of all answers (find subsets and permutations)
- Requires the traversal of paths in a matrix grid or graph
- Question is concerned with the actual solution values rather than the most optimum value of some parameter
( the latter would be solved with DP or greedy)

## Permutations and combinations
Difference between combination and permutation is the latter cares about the order of the elements while
the former does not.

### Combination template
```pydocstring
# find all combinations of any len that sums to target
def backtrack_comb_template(nums, target):
    res = []
    nums.sort() 
    def dfs(nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
                # skip duplicate paths
                if i > index and nums[i] == nums[i-1]: 
                    continue
                elif nums[i] > target:
                    break
                dfs(nums, target-candidates[i], i+1, path+[nums[i]], res)
        dfs(nums, target, 0, [], res)
        return res
```

### Permutation template
```pydocstring
# return all possible unique permutations
def backtrack_permute_template(nums: List[int]) -> List[List[int]]:
        res = []
        counter = Counter(nums)
        def backtrack(temp, counter):
            if len(nums) == len(temp):
                es.append(temp[:])
            # iterate possible values for the next permutation level
            for x in counter:
                # if not valid condition:
                    # ...
                if counter[x] > 0:
                    # add x to path and go through next permutation level
                    temp.append(x)
                    counter[x] -= 1
                    backtrack(temp, counter)
                    # remove last value x after already going through that 
                    # path. This makes room for the next paths for other values on the same permutation level
                    temp.pop() 
                    counter[x] += 1     
        backtrack([], counter)
        return res
```

### Permutation and combination questions:
```
39 Combination Sum
40. Combination Sum II
216. Combination Sum III

46. Permutations
47. Permutations II
491. Increasing Subsequences
386. Lexicographical Numbers
60. Permutation Sequence
1593. Split a String Into the Max Number of Unique Substrings
1079. Letter Tile Possibilities
```

## Backtrack dfs of matrix grid and graphs

### grid dfs template
```pydocstring
def dfs_grid_template(grid: List[List[str]]):
    m, n = len(grid), len(grid[0])   
    # ...
    def dfs(i, j, m, n):
         if 0 <= i < m and 0 <= j < n and other condition:
            # ... 
            # iterate all the valid adjacent positions
            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                dfs(r, c, m, n)
    
    for i in range(m):
        for j in range(n):
            if grid[i][j]: # meets some condition
                dfs(i,j, m, n)
                # ...
    # ...
    return # ...
```

### Grid dfs questions:
```
130. Surrounded Regions
200. Number of Islands
934. Shortest Bridge
1219. Path with Maximum Gold
733. Flood Fill
827. Making A Large Island
```

## Recursive dfs 
This subset of backtracking problems uses a dfs helper function to 
recursively build to the solution set. Unlike the problems above, these
problems are not returning a collection of answers but may utilize patterns from above
to solve

```
473. Matchsticks to Square  # looking for combinations that fill 4 buckets
526. Beautiful Arrangement  
1376. Time Needed to Inform All Employees
``` 

## Iterative backtrack (Subset problems)
This subset of backtracking problems does not use recursion to solve. Instead, these
problems requires the iteration of the input and on each iteration, we apply
the current element to all the previously seen values before this iteration.
These problems build all possible subsets by using and adding to already existing values in the subset.

### Subsets template
```pydocstring
# find all possible subsets in a set of distinct int
def backtrack_subset_template(nums):
    ret = [[]]
        for num in nums:
            ret += [sub+[num] for sub in ret]
        return ret
```

### Subsets problems:
```
78. Subsets
90. Subsets II
784. Letter Case Permutation
1291. Sequential Digits
```

## Other problems

```
# iteratively dfs
565. Array Nesting

# divide and conquer
395. Longest Substring with At Least K Repeating Characters
```