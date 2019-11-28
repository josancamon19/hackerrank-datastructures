def deleteNode(head, position):
    if position == 0:
        head = head.next
        return head
    current = head
    counter = 0

    while current:
        if counter + 1 == position:
            if current.next:
                current.next = current.next.next
                break
        counter += 1
        current = current.next
    return head
