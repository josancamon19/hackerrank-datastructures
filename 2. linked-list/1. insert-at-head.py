class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def insertNodeAtHead(head, data):
    new_node = SinglyLinkedListNode(data)
    if head:
        new_node.next = head
    head = new_node
    return head
