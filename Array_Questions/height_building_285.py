#You are given an array representing the heights of neighboring buildings on a city street, from east to west. The city assessor would like you to write an algorithm that returns how many of these buildings have a view of the setting sun, in order to properly value the street.

# For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the top floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

# Can you do this using just one forward pass through the array?
#look at which of the numbers is the highest. then go to the right side and take all buildings that are lower than it. then check that each building is greater than its value to the right. 
#if a number is larger than the number checked minus the number of buildings that have sun light.
# 
test_array=[3,7,8,3,6,1,9,6,4,1] 
# remember that 8 is the largest num and the start of what we care about. 
def buildings_with_sunlight(arr):
    buldings_list = list()
    #creates an empty list
    for height in arr:
        if buldings_list and buldings_list[-1] < height:
            buldings_list.pop()
        buldings_list.append(height)
    print(buldings_list)
    return buldings_list


        
buildings_with_sunlight(test_array)