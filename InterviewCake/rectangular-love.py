rectangle_1 = {
        'left_x': 1,
        'bottom_y': 5,
        'width': 10,
        'height': 4
        }

rectangle_2 = {
        'left_x': 5,
        'bottom_y': 4,
        'width': 4,
        'height': 3
        }

r3 = {
        'left_x': 1,
        'bottom_y': 1,
        'width': 2,
        'height': 2
        }

r4 = {
        'left_x': 3,
        'bottom_y': 3,
        'width': 2,
        'height': 2
        }

def find_x_overlap(rectangle_1, rectangle_2):
    r1_left_x = rectangle_1['left_x']
    r1_right_x = rectangle_1['width'] + r1_left_x

    r2_left_x = rectangle_2['left_x']
    r2_right_x = rectangle_2['width'] + r2_left_x

    if (r1_right_x <= r2_left_x) or (r2_right_x <= r1_left_x):
        return None

    return { 'left_x': max(r1_left_x, r2_left_x), 'width': abs(max(r1_left_x, r2_left_x) - min(r1_right_x, r2_right_x)) }

def find_y_overlap(rectangle_1, rectangle_2):
    r1_bottom_y = rectangle_1['bottom_y']
    r1_upper_y = rectangle_1['height'] + r1_bottom_y

    r2_bottom_y = rectangle_2['bottom_y']
    r2_upper_y = rectangle_2['height'] + r2_bottom_y

    if (r1_upper_y <= r2_bottom_y) or (r2_upper_y <= r1_bottom_y):
        return None

    return { 'bottom_y': max(r1_bottom_y, r2_bottom_y), 'height': abs(min(r1_upper_y, r2_upper_y) - max(r1_bottom_y, r2_bottom_y)) }

def find_intersection(rectangle_1, rectangle_2):
    x_intersection = find_x_overlap(rectangle_1, rectangle_2)
    if x_intersection == None:
        return None

    y_intersection = find_y_overlap(rectangle_1, rectangle_2)
    if y_intersection == None:
        return None

    return {
            'left_x': x_intersection['left_x'],
            'bottom_y': y_intersection['bottom_y'],
            'width': x_intersection['width'],
            'height': y_intersection['height']
            }

print find_intersection(r3, r4)
