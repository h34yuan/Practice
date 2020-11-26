# Stack
Stack is a linear data structure which follows the last in first out (LIFO) order.

(Note that queues and stacks are commonly used in other algorithms but 
this page is used to explain queue/stack specific questions and patterns)

## Patterns to look for:
- use a stack when the question needs to get things out in reverse order or
to compare some value with previously seen values in a most recent order.

## Stack on string questions
For theses problems, the questions involve the removal of some chars in a string, compute or modify
the string in some order or apply some operation on some parenthesized substring.
A stack is used keep track the available elements so far in the current iteration, the modified string/computed value so far.

```
224. Basic Calculator
227. Basic Calculator II
1209. Remove All Adjacent Duplicates in String II
402. Remove K Digits
844. Backspace String Compare
1190. Reverse Substrings Between Each Pair of Parentheses
1249. Minimum Remove to Make Valid Parentheses
1047. Remove All Adjacent Duplicates In String
394. Decode String
921. Minimum Add to Make Parentheses Valid
856. Score of Parentheses
```


## monotone increasing/decreasing stack
In a monotone stack, the top element must always be the largest/smallest value in a increasing/decreasing stack.
When adding an element to a increasing monotone stack, all the elements larger than the new entry must be popped
to ensure the monotonic order.
Questions indicate the results must be in some order or to keep track of inc/dec ordering.

```pydocstring
# template for monotone increasing stack
def mono_inc_stack_template(nums):
    stack = []
    # ...
    for x in nums:
        #...
        while stack and x < stack[-1]:
            stack.pop()
        stack.append(x)
        # ...
```

### Monotone stack questions
```
962. Maximum Width Ramp
456. 132 Pattern
84. Largest Rectangle in Histogram
1081. Smallest Subsequence of Distinct Characters
316. Remove Duplicate Letters
739. Daily Temperatures

# two stack, monotone min/max stack starting from each end of array
907. Sum of Subarray Minimums
```

## Other Questions
```
# comparing numerical values
735. Asteroid Collision
```

# Queue
Queue is a data structure that uses a first in first out (FIFO) ordering as the first
element added to the queue will also be the first item removed.

## Monotone queue
Similar to monotone stack as the order of the queue is increasing or decreasing

```
239. Sliding Window Maximum
```
