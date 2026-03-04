# array = [4, 10, 3, 5, 1]

class MinHeap:

    def __init__(self, array):
        self.array = self.build_heap(array)

    def build_heap(self, array):
        parent_idx = (len(array) - 1) // 2
        for current_idx in reversed(range(parent_idx)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array

    def sift_down(self, current_idx, end_idx, array):
        child_one_idx = (2 * current_idx) + 1
        while child_one_idx <= end_idx:
            child_two_idx = (2 * current_idx) + 2 if (2 * current_idx + 2) <= end_idx else -1
            if child_two_idx != -1 and array[child_two_idx] < array[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if array[idx_to_swap] < array[current_idx]:
                self.swap(current_idx, idx_to_swap, array)
                current_idx = idx_to_swap
                child_one_idx = (2 * current_idx) + 1
            else:
                break

    def sift_up(self, current_idx, array):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and array[current_idx] < array[parent_idx]:
            self.swap(parent_idx, current_idx, array)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2


    def swap(self, idx1, idx2, array):
        array[idx1], array[idx2] = array[idx2], array[idx1]

    def peek(self):
        return self.array[0]

    def remove(self):
        self.swap(0, len(self.array) - 1, self.array)
        value_to_remove = self.array.pop()
        self.sift_down(0, len(self.array) -1, self.array)
        return value_to_remove

    def insert(self, value):
        self.array.append(value)
        self.sift_up(len(self.array) - 1, self.array)


if __name__ == "__main__":
    array = [8, 12, 23, 17, 31, 30, 44, 102, 18]
    heap = MinHeap(array)

    print("Initial heap:", heap.array)

    heap.insert(5)
    print("After inserting 5:", heap.array)

    print("Peek:", heap.peek())

    print("Removing min:", heap.remove())
    print("Heap after removal:", heap.array)

