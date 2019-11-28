class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    current = head
    while current:
        if data < current.data:
            new_node.prev = current.prev
            new_node.next = current
            if current.prev:
                current.prev.next = new_node
            else:
                head = new_node
            current.prev = new_node
            break
        if current.next is None:
            current.next = new_node
            new_node.prev = current
            break
        current = current.next

    return head
