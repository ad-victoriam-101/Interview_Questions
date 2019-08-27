#given a 2d array, return the largest possible hourglass and the sum of the largest. 
#2 3 4
#x 3 y
#1 0 2
#an example of an hourglass. 
def hourglass_sum(arr):
    sum = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            
    print(max(sum))
