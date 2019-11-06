def inOrder(root):
    # Write your code here
    visit_order = list()

    def traverse(node):
        if node:
            traverse(node.left)
            visit_order.append(str(node.info))
            traverse(node.right)

    traverse(root)
    print(' '.join(visit_order))
