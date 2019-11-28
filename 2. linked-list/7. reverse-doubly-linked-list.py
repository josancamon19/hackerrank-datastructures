def reverse(head):
    current = head
    while current:
        current.next, current.prev = current.prev, current.next
        if current.prev is None:
            break
        current = current.prev
    return current
