def preOrder(root):
    # Write your code here
    visit_order = list()

    def traverse(node):
        if node:
            visit_order.append(str(node.info))
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    print(' '.join(visit_order))