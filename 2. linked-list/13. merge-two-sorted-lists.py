def mergeLists(head1, head2):
    node1 = head1
    node2 = head2
    prev1 = None
    while node1 and node2:
        if node1.data <= node2.data:
            prev1 = node1
            if node1.next is None:
                node1.next = node2
                break
            node1 = node1.next
        else:
            node2_next = node2.next
            node2.next = node1
            if prev1 is None:
                head1 = node2
            else:
                prev1.next = node2
            prev1 = node2

            node2 = node2_next

    return head1
