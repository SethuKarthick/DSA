values = [1, 2, 3, 4, 5]


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_linked_list(values):
    head = LinkedList(values[0])
    current =  head

    for v in values[1:]:
        current.next = LinkedList(v)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(str(current.value))
        current = current.next
    print(f"{' -> '.join(values)}")

def remove_kth_node_from_end(head, k):
    first = head
    second =  head

    for _ in range(k):
        second = second.next

    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while second.next:
        first = first.next
        second = second.next

    first.next = first.next.next


if __name__ == '__main__':
    head = build_linked_list(values)
    print_linked_list(head)
    remove_kth_node_from_end(head, 4)
    print_linked_list(head)

