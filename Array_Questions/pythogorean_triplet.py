#given an array of numbers check if any of them follow the pythogorean code of a^2 + b^2 = c^2
test_array = [2,6,6,7,8,8,9,10,12,13,5,12,13]

def pythogorean_trip(arr):
    squared = [x * x for x in arr]
    set_of_squares = set((squared))
    print (squared)
    print(set_of_squares)
    
    for i in range(len(squared) - 1):
        for k in range(i + 1,len(squared) - 1):
            summed = squared[i] + squared[k]
            print(summed,squared[i],squared[k])
            if summed in set_of_squares:
                return True
    return False


# pythogorean_trip(test_array)
def contains_pytrip(arr):
    squared = [x * x for x in arr]
    set_of_squares = set((squared))
    #remember that making a set removes the duplicates in a list. so this will have one of them. 
    print(squared)
    print(set_of_squares)
    for i in range(len(squared) - 1):
        for k in range(i + 1, len(squared) - 1):
            #this takes a range though each i adds 1 to it and though the length of the array. 
            summed = squared[i] + squared[k]
            print(summed,squared[i],squared[k])
            if summed in set_of_squares:
                print("True")
                return True

    return False


# Tests
contains_pytrip(test_array)
pythogorean_trip(test_array)