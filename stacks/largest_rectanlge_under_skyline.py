buildings = [1, 3, 3, 2, 4, 1]

def largest_rectangle_under_skyline(buildings):
    stack = []
    max_area = 0

    for idx in range(len(buildings) + 1):
        current_height = 0 if idx == len(buildings) else buildings[idx]

        while stack and current_height < buildings[stack[-1]]:
            height = buildings[stack.pop()]
            right = idx
            left = stack[-1] + 1 if stack else 0
            width = right - left
            area = height * width
            max_area = max(area, max_area)
        stack.append(idx)
    return max_area

res = largest_rectangle_under_skyline(buildings)
print(res)


