# You are given a string of length N and a parameter k. 
# The string can be manipulated by taking one of the first k letters and moving it to the end.

# Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

# For example, suppose we are given the string daily and k = 1. The best we can create in this case is ailyd.

test_string = "daily"

def lexicographically(str,k):
    k = int(k)
    # print(type(k))
    new_str = list(str[0:k])
    new_str.sort()
    start = new_str[0]
    
    



lexicographically(test_string,2)