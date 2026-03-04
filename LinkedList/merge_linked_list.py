class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_linked_lists(head_one: ListNode, head_two: ListNode):
    prev = None

    p1 = head_one
    p2 = head_two


    while p1 and p2:
        if p1.value < p2.value:
            prev = p1
            p1 = p1.next
        else:
            if prev is not None:
                prev.next = p2
            prev = p2
            p2 = p2.next
            prev.next = p1

    if p1 is None:
        prev.next = p2

    return head_one if head_one.value < head_two.value else head_two

def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)

    # List 2: 2 -> 4 -> 6
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)

    # Merge the two lists
    merged_list = merge_linked_lists(l1, l2)

    # Print the merged list
    print_linked_list(merged_list)

