nums1 = [1, 3, 8, 9, 15]
nums2 = [7, 11, 18, 19, 21, 25]

def get_median(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)

    left_size = (m+n+1) // 2

    low = 0
    high = m-1

    while low <= high:
        i = (low+high) // 2
        j = left_size - i

        a_left = nums1[i-1] if i >= 0 else float("-inf")
        a_right = nums1[i] if i < m else float("inf")

        b_left = nums2[j-1] if j >= 0 else float("-inf")
        b_right = nums2[j] if j < n else float("inf")

        if (a_left <= b_right) and (b_left <= a_right):
            if (m+n) % 2 == 1:
                return max(a_left, b_left)
            else:
                return (max(a_left, b_left) + min(a_right, b_right)) // 2

        elif a_left > b_right:
            high = i - 1
        else:
            low = i + 1

res = get_median(nums1, nums2)
print(res)
