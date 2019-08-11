# Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

# For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:
# Arrangement       |   Change
# ----------------------------------------
# ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
# ['B', 'B', 'G', 'B']      | (B, G) -> R
# ['B', 'R', 'B']           | (R, B) -> G
# ['B', 'G']                | (B, G) -> R
# ['R']                     |

sample_input = ['R', 'G', 'B', 'G', 'B']

def quxes_combiner(arr):
    for quexe in arr:
        if quexe != arr[quexe+1]:
            return
    return





######################################################################################################
COLORS = {"R", "G", "B"}
#create a set of all the colors in this test. (helpful for adding new colors later.)


def get_odd_man(col_a, col_b):
    return list(COLORS - set([col_a, col_b]))[0]
#this grabs the odd colors, aka the colors that don't exactly get transformed into new colors.


def minimize(quixes):
    stack = list()
    for quix in quixes:
        #for each item in the list(array) given, if the index doesn't add up to a new color, Put the current color in the set.
        if not stack or stack[-1] == quix:
            stack.append(quix)
            continue

        new = get_odd_man(quix, stack[-1])
        stack.pop()
        stack.append(new)
        while len(stack) > 1 and stack[-1] != stack[-2]:
            a, b = stack.pop(), stack.pop()
            stack.append(get_odd_man(a, b))
    
    print(stack)
    return stack


# Tests
assert minimize(["R", "G", "B", "G", "B"]) == ["R"]