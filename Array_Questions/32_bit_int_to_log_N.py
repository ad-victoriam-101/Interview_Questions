# Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.
#For these things you gotta tak etime. 

# Function to check if x is power of 4 
def isPowerOfFour(number_test): 
    if (number_test == 0): 
        return False
    while (number_test != 1): 
            if (number_test % 4 != 0): 
                return False
            number_test = number_test // 4
              
    return True
  
# Driver code 
#want to update to take user input.

test_no = 8888
if(isPowerOfFour(64)): 
    print(test_no, 'is a power of 4') 
else: 
    print(test_no, 'is not a power of 4') 
  