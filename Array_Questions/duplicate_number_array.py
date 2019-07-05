#python test quesions
# given an array of numbers find the missing one. 
import random
test_array = []
def fill_array():
    #generates a new array of 1-100
    for number in range(101):
        test_array.append(number)
def array_pop():
    #generates a random index and inserts it in test_array
    for x in range(1):
        random_int = random.randint(1,101)
        print(random_int)
        test_array.insert(random_int,random_int)

def print_repeating(array,size_of_array):
    #takes an array and the size of said array to find the duplicate number. 
    for i in range(0,size_of_array):
        if array[i] == array[i-1]:
            print("The Repeating number is: ",array[i])

fill_array()
array_pop()
array_length = len(test_array)
print(test_array)
print(array_length)
print_repeating(test_array,array_length)
#missing_number(test_array)
#thoughts on this section, Really messed up the print repeating call, Make sure the function being called doesn't contain a function in it


