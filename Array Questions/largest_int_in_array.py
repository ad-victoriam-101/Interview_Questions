import random
test_array = []
def fill_array():
    for i in range(0,101):
        random_int = random.randint(1,1001)
        test_array.append(random_int)
fill_array()
def largest_num(arr):
    max_int = arr[0]
    for i in range(0,len(arr)):
        if arr[i] > max_int:
            max_int = arr[i]
    return max_int
    
print("The largest int is: ",largest_num(test_array))

print(test_array)