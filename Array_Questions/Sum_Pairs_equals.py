#how would you find all pairs of an integer array who's sum is equal to a given number.
import random
test_array = []
target_sum = 500
numbers_sum = []
def fill_array():
    #fills an empty array with 100 random numbers from 1-1000
    for i in range(0,101):
        random_int = random.randint(1,1001)
        test_array.append(random_int)
def sum_pairs_func(arr,target_sum):
    count = 0
    for i in range (0,len(arr)):
        for j in range (i+1,len(arr)):
            if arr[i] + arr[j] == target_sum:
                numbers_sum.append(arr[i])
                numbers_sum.append(arr[j])
                count += 1
    return count 



fill_array()
print(sum_pairs_func(test_array,target_sum))
print(numbers_sum)
print(test_array)

