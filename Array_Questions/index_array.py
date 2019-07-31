# A fixed point in an array is an element whose value is equal to its index. 
# Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.
# For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
test_array = [-6,0,2,40]
def array_index_test(array):
    for i in range(len(array)):
        if array[i] is i:
            return i
    return False