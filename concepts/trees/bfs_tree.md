# Bfs tree traversal
Breadth first search (bfs) traversal of a binary tree structure is when we start from the root and traverse all the nodes
on the current level before moving on to the next level. Bfs uses a queue to keep track of the order of nodes.

### Tree data structure
```pydocstring
class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
```

## Patterns to look for:
- question asks to find/compute values specific to each level
- question asks to find the position of some nodes based on its level
- question asks for the shortest path to some node

## Bfs tree traversal template
```pydocstring
def bfs_levels_template(root):
    if root is None:
        return
    q = [root]
    while len(q) > 0:
        level_size = len(q) # level order only
        level = [] # level order only
        for i in range(level_size): # level order only
            temp = q.pop(0)
            level.append(temp.data) # level order only
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
```

## Bfs tree questions:
```
653. Two Sum IV - Input is a BST
1161. Maximum level sum of a binary tree
958. Check Completeness of a Binary Tree
951. Flip Equivalent Binary Trees
513. Find Bottom Left Tree Value
429. N-ary Tree Level Order Traversal
1372. Longest ZigZag Path in a Binary Tree

# using stack
129.r Sum Root to Leaf Numbers
116. Populating Next Right Pointers in Each Node
```