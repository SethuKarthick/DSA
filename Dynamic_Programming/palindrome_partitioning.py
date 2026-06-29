string = "noonabbad"

def palindrome_partitioning(string):

    n = len(string)

    palindromes = [[False] * n for _ in range(n)]

    for i in range(n):
        palindromes[i][i] = True


    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length  - 1

            if length == 2:
                palindromes[i][j] = string[i] == string[j]

            else:
                palindromes[i][j] = string[i] == string[j] and palindromes[i+1][j-1]

    cuts = [float("inf") for _ in range(n)]

    for i in range(n):
        if palindromes[0][i]:
            cuts[i] = 0

        else:
            for j in range(i):
                if palindromes[j+1][i]:
                    cuts[i] = min(cuts[i], cuts[j] + 1)

    return cuts[-1]

res = palindrome_partitioning(string)
print(res)








