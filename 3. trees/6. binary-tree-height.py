def height(root):
    if root is None:
        return 0
    return height_helper(root)


def height_helper(node, counter=0):
    if node:
        left_counter = height_helper(node.left, counter + 1)
        right_counter = height_helper(node.right, counter + 1)
        return max(left_counter, right_counter)
    return counter - 1
