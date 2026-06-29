strings = ["a", "b", "ba", "bca", "bda", "bdca"]

def get_longest_string_chains(strings):
    strings.sort(key = len)

    string_chains = {}

    for string in strings:
        string_chains[string] = {"next_string": "", "max_length": 1}


    max_string_length = 0
    max_string = ""

    for string in strings:
        for i in range(len(string)):
            smaller_string = string[:i] + string[i+1:]

            if smaller_string in string_chains:
                update_string_chains(string_chains, smaller_string, string)

        if string_chains[string]["max_length"] > max_string_length:
            max_string_length = string_chains[string]["max_length"]
            max_string = string

    return build_chain(string_chains, max_string)

def build_chain(string_chains, start_string):

    last_string_chains = []
    while start_string != "":
        last_string_chains.append(start_string)
        start_string = string_chains[start_string]["next_string"]

    return last_string_chains



def update_string_chains(string_chains, smaller_string, current_string):
    smaller_string_length = string_chains[smaller_string]["max_length"]
    current_string_length = string_chains[current_string]["max_length"]

    if smaller_string_length + 1 > current_string_length:
        string_chains[current_string]["next_string"] = smaller_string
        string_chains[current_string]["max_length"] = smaller_string_length + 1




res = get_longest_string_chains(strings)
print(res)
