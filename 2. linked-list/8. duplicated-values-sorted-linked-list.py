def removeDuplicates(head):
    current = head
    while current:
        current2 = current.next
        while current2 and current.data == current2.data:
            current2 = current2.next
        current.next = current2
        current = current.next
    return head
