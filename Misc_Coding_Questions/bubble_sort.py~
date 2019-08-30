#given an array, implement bubble sort. 
#This is a very slow sorting algorithm compared to algorithms like quicksort, with worst-case complexity O(n^2). 
#However, the tradeoff is that bubble sort is one of the easiest sorting algorithms to implement from scratch.
import random
test_array = []
for i in range(101):
    test_array.append(random.randint(1,101))
print(test_array)

def bubble_sort(test_list):
    for passnum in range(len(test_list)-1,0,-1):
        for i in range(passnum):
            if test_list[i] > test_list[i+1]:
                temp = test_list[i]
                test_list[i] = test_list[i+1]
                test_list[i+1] = temp

bubble_sort(test_array)
print(test_array)