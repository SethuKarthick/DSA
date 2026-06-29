matrix = [
  [5, 3, -1, 5],
  [-7, 3, 7, 4],
  [12, 8, 0, 0],
  [1, -8, -8, 2]
]

k = 2


def max_sum_subarray_matrix(matrix, k):
    sums = construct_sums(matrix, k)
    max_sum = get_max_sum(sums, matrix, k)
    return max_sum

def get_max_sum(sums, matrix, k):
    total_sum = float("-inf")

    for i in range(k-1, len(matrix)):
        for j in range(k-1, len(matrix[0])):

            current_sum = sums[i][j]

            if i - k >=0:
                current_sum -= sums[i-k][j]

            if j - k >= 0:
                current_sum -= sums[i][j-k]

            if i-k >=0 and j-k >=0:
                current_sum += sums[i-k][j-k]

            total_sum = max(total_sum, current_sum)

    return total_sum


def construct_sums(matrix, k):
    sums = [[0] * len(matrix[row]) for row in range(len(matrix))]
    sums[0][0] = matrix[0][0]

    for j in range(1, len(matrix[0])):
        sums[0][j] = matrix[0][j] + sums[0][j-1]

    for i in range(1, len(matrix)):
        sums[i][0] = matrix[i][0] + sums[i-1][0]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + matrix[i][j]

    return sums


res = max_sum_subarray_matrix(matrix, k)
print(res)