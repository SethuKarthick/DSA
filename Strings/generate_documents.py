characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

def generate_documents(characters, document):

    char_counts = {}
    for char in characters:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in document:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1
    return True

res = generate_documents(characters, document)
print(res)