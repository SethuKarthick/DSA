string = "AAAAAAAAAAAAABBCCCCDD"

def run_length_encoding(string):
    encoded = []
    count = 1

    for i in range(1, len(string)):
        prev_char = string[i - 1]
        current = string[i]

        if (prev_char != current) or count == 9:
            encoded.append(str(count))
            encoded.append(prev_char)
            count = 1
        else:
            count += 1
    encoded.append(str(count))
    encoded.append(string[-1])
    return "".join(encoded)

res = run_length_encoding(string)
print(res)
