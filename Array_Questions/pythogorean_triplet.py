#given an array of numbers check if any of them follow the pythogorean code of a^2 + b^2 = c^2
test_array = [2,3,4,5,6,6,7,8,8,9,10,12,13,5,12,13]

def triplet_test(array):
    for i in range(len(array)-2):
        if array[i]**2 + array[i+1]**2 == array[i+2]**2:
            print("the following numbers are triplets:",array[i],array[i+1],array[i+2])

triplet_test(test_array)