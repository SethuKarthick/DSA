def lcs_hirschberg(str1, str2):
    def lcs_length(s1, s2):
        m, n = len(s1), len(s2)
        prev = [0] * (n + 1)
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev

    def hirschberg(s1, s2):
        if not s1:
            return ""
        if len(s1) == 1:
            return s1 if s1 in s2 else ""

        mid = len(s1) // 2
        left = lcs_length(s1[:mid], s2)
        right = lcs_length(s1[mid:][::-1], s2[::-1])[::-1]

        k = max(range(len(s2) + 1), key=lambda x: left[x] + right[x])

        return hirschberg(s1[:mid], s2[:k]) + hirschberg(s1[mid:], s2[k:])

    return hirschberg(str1, str2)

# Example
str1 = "ABCDGH"
str2 = "AEDFHR"
result = lcs_hirschberg(str1, str2)
print(result)  # Output: "ADH"


# lCS count -->
#
# s1 = "ABCDGH"
# s2 = "AEDFHR"
#
#
#
# def get_lcs_count(s1, s2):
#     prev = [0] * (len(s2) + 1)
#
#     for i in range(1, len(s1) + 1):
#         current = [0] * (len(s2) + 1)
#         for j in range(1, len(s2) + 1):
#             if s1[i-1] == s2[j-1]:
#                 current[j] = prev[j-1] + 1
#             else:
#                 current[j] = max(current[j-1], prev[j])
#
#         prev = current
#
#     return prev[-1]
#
#
# # res = get_lcs_count(s1, s2)
# # print(res)
#
#
#
#
# def edit_distance(s1, s2):
#     prev = list(range(len(s2)+1))
#
#     for i in range(1, len(s1)+1):
#         current = [0] * (len(s2) + 1)
#         current[0] = i
#         for j in range(1, len(s2)+1):
#             if s1[i-1] == s2[j-1]:
#                 current[j] = prev[j-1]
#             else:
#                 current[j] = 1+ min(prev[j], current[j-1], prev[j-1])
#         prev = current
#
#     return prev[-1]
#
# res = edit_distance(s1, s2)
# print(res)
#





