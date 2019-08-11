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
            