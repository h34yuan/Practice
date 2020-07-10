# Balanced tree: not exactly the same size on subtrees but with O(logn) times
# Complete binary tree: last level is filled left to right
# Full binary tree: every node has either zero or two child nodes
# Perfect binary trees: full and complete
# Tries: variant of an n-ary tree where a character is stored at each node. each path down the tree until a null node
# represents a word. A node can have 1 to alphabet_size + 1 children


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


def bfs(root):
    if root is None:
        return
    q = []
    temp = root
    while temp:
        print(temp.data)
        q.append(temp.left)
        q.append(temp.right)
        temp = q.pop(0)


def bfs2(root):
    if root is None:
        return
    q = []
    q.append(root)
    while len(q) > 0:
        temp = q.pop(0)
        print(temp.data)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

def bfs_levels(root):
    if root is None:
        return
    q = [root]
    while len(q) > 0:
        level_size = len(q)
        level = []
        # goes through all nodes in current level
        for i in range(level_size):
            temp = q.pop(0)
            level.append(temp.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        print(level)


# count nodes dfs left and right
def countNodes(self, root) -> int:
    if not root:
        return 0
    left_depth = self.getDepth(root.left)
    right_depth = self.getDepth(root.right)
    if left_depth == right_depth:
        return pow(2, left_depth) + self.countNodes(root.right)
    else:
        return pow(2, right_depth) + self.countNodes(root.left)

def getDepth(self, root):
    if not root:
        return 0
    print(root.val)
    return self.getDepth(root.left) + 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # inorder_traversal(root)
    # preorder_traversal(root)
    # postorder_traversal(root)
    # bfs2(root)
    bfs_levels(root)