def print_linked_list(head):
    if head is None:
        return

    current = head
    while current:
        print(current.data)
        current = current.next
