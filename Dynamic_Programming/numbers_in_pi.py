

pi = "3141592653589793238462643383279"

numbers = [
  "314159265358979323846",
  "26433",
  "8",
  "3279",
  "314159265",
  "35897932384626433832",
  "79"
]

def get_min_spaces(pi, numbers):
    numbers_set = set(numbers)
    cache = {}

    def helper(idx):

        if idx == len(pi):
            return -1

        if idx in cache:
            return cache[idx]

        min_spaces = float("inf")

        for i in range(idx, len(pi)):
            prefix = pi[idx: i+1]
            if prefix in numbers_set:
                spaces_in_prefix = helper(i+1)
                if spaces_in_prefix != float("inf"):
                    min_spaces = min(min_spaces, spaces_in_prefix + 1)

        cache[idx] = min_spaces
        return min_spaces

    result = helper(0)
    return result if result != float("inf") else -1

res = get_min_spaces(pi, numbers)
print(res)




