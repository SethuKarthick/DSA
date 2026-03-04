values = [1, 1, 3, 4, 4, 4, 5]

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

def print_linked_list(head):
    values = []
    current =  head
    while current is not None:
        values.append(str(current.value))
        current = current.next
    print(f"{' -> '.join(values)}")

def remove_duplicates(head):
    current = head

    while current:
        next_distinct = current.next
        while next_distinct and next_distinct.value == current.value:
            next_distinct = next_distinct.next

        current.next = next_distinct
        current = next_distinct

    return head


if __name__ == "__main__":
    head = build_linked_list(values)
    print_linked_list(head)
    remove_duplicates(head)
    print_linked_list(head)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            next_distinct = current.next
            while next_distinct and next_distinct.val == current.val:
                next_distinct = next_distinct.next

                # current.next = next_distinct
            if current.next == next_distinct:
                prev = current
            else:
                prev.next = next_distinct

            current = next_distinct
        return dummy.next