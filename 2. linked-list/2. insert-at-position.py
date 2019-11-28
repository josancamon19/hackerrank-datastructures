class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    if position == 0:
        node.next = head
        head = node
        return head
    current = head
    counter = 0
    while current:
        if counter + 1 == position:
            node.next = current.next
            current.next = node
            break
        counter += 1
        current = current.next
    return head
