class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def shift_linked_list(head: ListNode, k : int) -> ListNode:
    if not head or k == 0:
        return head

    current = head
    length = 1
    while current.next:
        current = current.next
        length += 1

    k = k % length
    if k == 0:
        return head

    current = head
    for _ in range(length - k - 1):
        current = current.next

    new_head = current.next
    current.next = None

    new_tail = new_head
    while new_tail.next:
        new_tail = new_tail.next

    new_tail.next = head

    return new_head

def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Shift the list by 2 positions
    shifted_list = shift_linked_list(head, 2)

    # Print the shifted list
    print_linked_list(shifted_list)




