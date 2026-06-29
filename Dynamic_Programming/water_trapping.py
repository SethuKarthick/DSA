heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]

def get_amount_of_water_trapped(heights):
    maxs = [0] * len(heights)
    left_max = heights[0]

    for i in range(len(heights)):
        height = heights[i]
        maxs[i] = left_max
        left_max = max(left_max, height)

    right_max = heights[-1]
    for i in range(len(heights)-1, -1, -1):
        height = heights[i]
        min_height = min(right_max, maxs[i])
        if height < min_height:
            maxs[i] = min_height - height
        else:
            maxs[i] = 0
        right_max = max(right_max, height)

    return sum(maxs)

def get_water_amount(heights):

    left = 0
    right = len(heights) - 1

    water = 0

    left_max = heights[left]
    right_max = heights[right]

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
    return water





res = get_water_amount(heights)
print(res)