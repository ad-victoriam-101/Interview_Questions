# Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.

# On the ith jump, you may move exactly i places to the left or right.

# Find a path with the fewest number of jumps required to get from 0 to N.
n = int(input("please enter a number: "))

def jump_to_target(num):
    abs_num = abs(num)
    if abs_num < 2:
        return abs_num

    point, new_point = None, 0
    jump = 1
    while new_point <= abs_num:
        point = new_point
        new_point += jump
        jump += 1
    jump -= 2
    return (2 * (abs_num - point)) + jump

print(jump_to_target(n))
        