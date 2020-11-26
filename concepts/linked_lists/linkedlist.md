# Linked List
A linked list is a linear data structure where the elements are not stored at contiguous memory locations by
are linked using pointers. Each node will contain a data field and a reference to the next node in the list.

### Linked list node data structure
```pydocstring
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
```

## Multiple pointers
In this subset of problems, multiple pointers may be needed to keep track of the different positions of the linked lists.
In these problems, a pointer is usually initialized to point at the first node of the linked list which does not move
and is returned after the traversal as that pointer returns the entire linked list.
Usually a dummy node may be initialized and set before the head where another pointer (pre) starts at dummy
to keep track of left bound (previous position) while the cur that traverses the linked list represent the right bound.


### Patterns to look for:
- question asks to remove elements from linked list
- question asks to reorder the linked list (e.g. reverse, rotate)
(Also know as in-place reversal of linked list)

### Template example:
```pydocstring
# reverse the linked list between node m and n
def reverse_between_template(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        # find the node before reversal
        for i in range(m-1):
            pre = pre.next
            
        curr, reverse  = pre.next, None
        # reverse the nodes between m and n
        for i in range(n-m+1):
            curr.next, reverse, curr = reverse, curr, curr.next

        # set the next of the last reversal to n+1 (the mth element is the last element in the reversal)
        pre.next.next = curr
        # set m-1.next to reverse (the nth element is the first element in the reversal)
        pre.next = reverse
        return dummy.next
```

### Multiple pointer questions:
```
83. Remove Duplicates from Sorted List
82. Remove Duplicates from Sorted List II
86. Partition List
725. Split Linked List in Parts

## rotate/reverse list
206. Reverse Linked List
92. Reverse Linked List II
61. Rotate List

## two linked lists
160. Intersection of Two Linked Lists
445. Add Two Numbers II
```

## Fast slow pointers
The fast slow pointer is a pointer algorithm that uses two pointer which moves through the linear data structure
(array, linked list) at different speeds. This is useful for dealing with cyclic linked lists or arrays.
 With the pointers moving at different speeds in a cyclic linked list, the pointers are bound to meet as the fast pointer 
 will catch the slow pointer in a cylic loop.
 
### Patterns to look for:
- problem deals with a loop in a linked list or array
- looking for the position of a certain element or overall length

### Fast slow pointer template:
```pydocstring
def fast_slow_template(head: ListNode):
    fast = head
    slow = head
    # ...
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # ...
    return slow
```

### Fast slow pointer questions:
```
876. Middle of the Linked List
141. Linked List Cycle
109. Convert Sorted List to Binary Search Tree
328. Odd Even Linked List
```