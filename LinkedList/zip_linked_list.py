class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrange_linked_list(head: ListNode) -> ListNode:

    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    second_half = slow.next
    slow.next = None

    prev = None
    current = second_half
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    second_half = prev

    first_half = head
    while second_half:
        temp1 = first_half.next
        temp2 = second_half.next

        first_half.next = second_half
        second_half.next = temp1

        first_half = temp1
        second_half = temp2

    return head

def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # Create the linked list 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Rearrange the linked list
    rearranged_list = rearrange_linked_list(head)

    # Print the rearranged list
    print_linked_list(rearranged_list)



