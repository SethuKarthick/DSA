

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head: ListNode):
    if not head:
        return False

    first = head
    second = head

    while second != second.next:
        first = first.next
        second = second.next.next

        if first == second:
            break

    else:
        return False

    first = head

    while first != second:
        first = first.next
        second = second.next

    return first

if __name__ == "__main__":
    # Example usage:
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next  # Creates a cycle (4 -> 2)

    cycle_start = has_cycle(head)
    if cycle_start:
        print(f"Cycle detected at node with value: {cycle_start.value}")
    else:
        print("No cycle detected.")


