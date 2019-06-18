#python test quesions
# given an array of numbers find the missing one. 
import random
test_array = []
def fill_array():
    #generates a new array of 1-100
    for number in range(101):
        test_array.append(number)
def array_pop():
    #generates a random index and pops it out of test_array
    for x in range(1):
        random_int = random.randint(1,101)
        print(random_int)
        test_array.insert(random_int,random_int)
def missing_number(test_arrays):
    #this is a guassian formula that is implemented in python to find the missing number. 
    n = len(test_arrays)
    total = ((n)*(n+1))/2
    sum_of_array = sum(test_arrays)
    missing = total - sum_of_array
    print("the missing number is:",missing)
fill_array()
array_pop()
print(test_array)
#missing_number(test_array)
