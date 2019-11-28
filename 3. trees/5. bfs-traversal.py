def levelOrder(root):
    queue = [root]
    visited = []
    while len(queue) > 0:
        node = queue.pop()
        visited.append(str(node.info))
        if node.left:
            queue.insert(0, node.left)
        if node.right:
            queue.insert(0, node.right)
    print(' '.join(visited))
