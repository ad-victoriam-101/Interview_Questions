#For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. 
# For example, c = [0,1,0,0,0,1,0] indexed from 0 - 6. The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . 
# She could follow the following two paths:  or . The first path takes jumps while the second takes .
clouds = [0,1,0,0,0,1,0]
def cloud_jumper(arr):
    jumps, i = 0,0
    while i < len(arr)-1:
        # if 2 cloud jumps
        if i+2 < len(arr) and arr[i+2] != 1:
            # print(i)
            #first checks that the number we're checking is in bounds, and that you can make a double jump, if you can change the i possition to reflect a double jump. 
            i += 1
        jumps += 1
        i += 1
    return jumps

print(cloud_jumper(clouds))