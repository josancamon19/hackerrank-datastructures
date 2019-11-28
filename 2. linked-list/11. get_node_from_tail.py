def getNode(head, positionFromTail):
    first = second = head
    counter = 0
    while second and counter < positionFromTail:
        counter += 1
        second = second.next

    while second.next:
        second = second.next
        first = first.next
    return first.data
