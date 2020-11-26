# Dfs tree traversal
Depth first search (dfs) is a technique used for traversing all the nodes in a tree.
This algorithm starts at the root node and explores to the deepest node possible along each branch
,then backtracks until it finds an unexplored path, and explores it until all nodes are visited.
Dfs can be implemented through recursion or with a stack.

### Tree data structure
```pydocstring
class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
```

## Types of Dfs
There are 3 different ways to use dfs to traverse a tree. 
1.Inorder: traverses left, root, right
2.Preorder: traverses root, left, right
3.Postorder: traverses left, right, root

```pydocstring
class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder_traversal(root):
    # left root right
    if root:
        inorder_traversal(root.left)
        print(root.data),
        inorder_traversal(root.right)

def preorder_traversal(root):
    # root left right
    if root:
        print(root.data)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    # left right root
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data)
``` 

## Patterns to look for:
- looking for the depth or path of some nodes
- searching for some node or position in a tree
- requires traversal of entire tree (dfs is faster and uses less space than bfs)

## Dfs questions:
```
# dfs general
1022. Sum of Root To Leaf Binary Numbers
95. Unique Binary Search Trees II
669. Trim a Binary Search Tree
1315. Sum of Nodes with Even-Valued Grandparent
508. Most Frequent Subtree Sum
701. Insert into a Binary Search Tree
988. Smallest String Starting From Leaf
938. Range Sum of BST

# in order
687. Longest Univalue Path
1305. All Elements in Two Binary Search Trees
1302. Deepest Leaves Sum
222. Count complete Tree Nodes
543. Diameter of binary tree
965. Univalued Binary Tree
993. Cousins in Binary Tree
124. Binary Tree Maximum Path Sum [dfs compare max sum of left and right subtrees]
1382. Balance a Binary Search Tree
1325. Delete Leaves With a Given Value
530. Minimum Absolute Difference in BST
814. Binary Tree Pruning
1038. Binary Search Tree to Greater Sum Tree
538. Convert BST to Greater Tree
783. Minimum Distance Between BST Nodes
501. Find Mode in Binary Search Tree

# post order
145. Binary Tree Postorder Traversal
590. N-ary Tree Postorder Traversal
652. Find Duplicate Subtrees

# pre order
297. Serialize and Deserialize Binary Tree
1008. Construct Binary Search Tree from Preorder Traversal
```