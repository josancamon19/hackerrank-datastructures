def reverse(node):
    prev = None
    current = node
    while current:
        n_next = current.next
        current.next = prev
        prev = current
        if n_next is None:
            break
        current = n_next

    return current
