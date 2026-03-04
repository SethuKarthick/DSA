class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrage_linked_list(head: ListNode, k:int) -> ListNode:
    less_head = less_tail = None
    equal_head = equal_tail = None
    greater_head = greater_tail = None

    current = head
    while current:
        next_node = current.next
        current.next = None

        if current.value < k:
            if not less_head:
                less_head = less_tail = current
            else:
                less_tail.next = current
                less_tail = current
        elif current.value == k:
            if not equal_head:
                equal_head = equal_tail = current
            else:
                equal_tail.next = current
                equal_tail = current
        else:
            if not greater_head:
                greater_head = greater_tail = current
            else:
                greater_tail.next = current
                greater_tail = current

        current = next_node

    head = tail = None
    for part in [less_head, equal_head, greater_head]:
        if part:
            if not head:
                head = part
                tail = part
                while tail.next:
                    tail = tail.next
            else:
                tail.next = part
                while tail.next:
                    tail = tail.next
    return head

def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

if __name__ == '__main__':
    values = [3, 0, 5, 2, 1, 4]
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    # Rearrange with pivot k = 3
    new_head = rearrage_linked_list(head, 3)

    # Print result
    print_linked_list(new_head)