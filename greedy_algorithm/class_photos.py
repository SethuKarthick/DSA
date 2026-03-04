red = [5, 8, 1, 3, 4]
blue = [6, 9, 2, 4, 5]

def class_photos(red, blue):

    red.sort()
    blue.sort()

    is_red_first = red[0] < blue[0]

    for i in range(len(red)):

        red_height = red[i]
        blue_height = blue[i]

        if is_red_first:
            if red_height >= blue_height:
                return False
        else:
            if blue_height >= red_height:
                return False

    return True

res = class_photos(red, blue)
print(res)
