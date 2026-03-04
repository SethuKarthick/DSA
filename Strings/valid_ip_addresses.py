string = "25525511135"

def valid_ips(string):
    ip_found = []

    for i in range(1, min(len(string), 4)):
        current_ip = ["", "", "", ""]
        current_ip[0] = string[:i]
        if not is_valid(current_ip[0]):
            continue
        for j in range(i+1, i + min(4, len(string)-i)):
            current_ip[1] = string[i:j]
            if not is_valid(current_ip[1]):
                continue
            for k in range(j+1, j + min(4, len(string)-j)):
                current_ip[2] = string[j:k]
                current_ip[3] = string[k:]
                if is_valid(current_ip[2]) and is_valid(current_ip[3]):
                    ip_found.append(".".join(current_ip))

    return ip_found


def is_valid(ip_part):
    int_ip  = int(ip_part)

    if int_ip > 255:
        return False
    return len(ip_part) == len(str(int_ip))

res = valid_ips(string)
print(res)
