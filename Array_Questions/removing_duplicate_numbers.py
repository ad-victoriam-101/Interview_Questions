#given an array remove all douplicate numbers from said array. 
import random
test_array = []
def fill_array():
    for i in range(0,101):
        random_int = random.randint(1,1001)
        test_array.append(random_int)
fill_array()
x = [1,2,3,4,4,5,6,7,8,8,]

def remove_dup(arr):
    for i in range(0,len(arr)):
        if i == (i+1):
            arr.pop(i)
            print("the duplicate number: ",i, "has been removed.")

print(test_array)
remove_dup(test_array)
remove_dup(x)
