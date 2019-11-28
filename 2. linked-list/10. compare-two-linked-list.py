def compare_lists(llist1, llist2):
    current1 = llist1
    current2 = llist2
    while current1 and current2:
        if current1.data != current2.data:
            return 0
        current1 = current1.next
        current2 = current2.next

    return current1 is None and current2 is None
