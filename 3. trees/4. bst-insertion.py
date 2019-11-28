class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root is None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        # Enter you code here.
        if self.root is None:
            self.root = Node(val)
            return
        insert_helper(self.root, val)


def insert_helper(node, val):
    if val < node.info:
        if node.left:
            insert_helper(node.left, val)
        else:
            node.left = Node(val)
    elif val > node.info:
        if node.right:
            insert_helper(node.right, val)
        else:
            node.right = Node(val)
    else:
        return
