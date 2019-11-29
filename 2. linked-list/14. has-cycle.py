def has_cycle(head):
    first = second = head
    while first and second:
        first = first.next
        if second.next is None:
            return False
        second = second.next.next
        if first == second:
            return True
    return False
