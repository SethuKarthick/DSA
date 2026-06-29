string='testthis is testtest to see if testtesttest it works'
substring='test'


def underscorify_substring(string, substring):

    locations = get_locations(string, substring)
    collated_locations = collate_locations(locations)
    return underscorify_substrings(collated_locations, string)

def get_locations(string, substring):
    start_idx = 0
    locations = []

    while start_idx < len(string):
        next_idx = string.find(substring, start_idx)

        if next_idx != -1:
            start_idx = next_idx + 1
            locations.append([next_idx, next_idx + len(substring)])
        else:
            break
    return locations

def collate_locations(locations):
    new_locations = [locations[0]]

    for i in range(1, len(locations)):
        prev = new_locations[-1]
        current = locations[i]

        if current[0] <= prev[1]:
            prev[1] = max(prev[1], current[1])
        else:
            new_locations.append(current)
    return new_locations

def underscorify_substrings(locations, string):
    location_idx = 0
    string_idx = 0
    final_char = []
    in_between_underscore = False

    while string_idx < len(string) and location_idx < len(locations):
        if string_idx == locations[location_idx][0]:
            if not in_between_underscore:
                final_char.append("_")
                in_between_underscore = True
        if string_idx == locations[location_idx][1]:
            final_char.append("_")
            in_between_underscore = False
            location_idx += 1
        final_char.append(string[string_idx])
        string_idx += 1

    if in_between_underscore:
        final_char.append("_")
    if string_idx < len(string):
        final_char.append(string[string_idx:])

    return "".join(final_char)


res = underscorify_substring(string, substring)
print(res)



