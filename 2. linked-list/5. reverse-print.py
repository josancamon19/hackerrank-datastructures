def reversePrint(node):
    if node:
        reversePrint(node.next)
        print(node.data)
