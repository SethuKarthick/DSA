

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def build_linked_list(values):
    head = LinkedList(values[0])
    current = head
    for v in values[1:]:
        current.next = LinkedList(v)
        current = current.next
    return head

def sum_linked_list(linked_list1, linked_list2):
    dummy_head = LinkedList(0)
    current = dummy_head
    p1 = linked_list1
    p2 = linked_list2
    carry = 0

    while p1 or p2 or carry:
        p1_value = p1.value if p1 else 0
        p2_value = p2.value if p2 else 0

        total = p1_value + p2_value + carry
        carry = total // 10
        new_node = LinkedList(total % 10)
        current.next = new_node
        current = new_node

        if p1: p1 = p1.next
        if p2: p2 = p2.next
    return dummy_head.next


def printLinkedList(head):
    values = []
    while head:
        values.append(str(head.value))
        head = head.next
    print(" → ".join(values))

if __name__ == "__main__":
    values1 = [1, 2, 3, 4, 5]
    values2 = [4, 5, 6, 7, 8]
    head1 = build_linked_list(values1)
    head2 = build_linked_list(values2)
    res = sum_linked_list(head1, head2)
    printLinkedList(res)
