#given an array of numbers check if any of them follow the pythogorean code of a^2 + b^2 = c^2
test_array = [2,3,4,5,6,6,7,8,8,9,10,12,13,5,12,13]

def pythogorean_trip(arr):
    num_squared = [x * x for x in arr]
    set_of_squares = set(num_squared)
    for i in range(len(num_squared)-1):
        for k in range(i+1,len(num_squared)-1):
            summed = num_squared[i] + num_squared[k]
            if summed in set_of_squares:
                print(i,k,summed,": are triplets.")
                return True
        return False

