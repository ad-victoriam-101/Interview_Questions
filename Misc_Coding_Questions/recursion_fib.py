#write a firbinachy sequence that takes a user input and then generates all sequences to that point. 
FibArray = [0,1] 
  
def fibonacci(n): 
    #test sequence makes sure the test is only preformed on proper inputs.

    if n<0: 
        print("Incorrect input") 
    elif n<=len(FibArray): 
        #same idea you don't need to actually calculate the sum of 2 numbers as they are already set.

        return FibArray[n-1] 
    else: 
        #if the input passes all our checks we then can start calculating the sequence. 

        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        
        FibArray.append(temp_fib) 
        return temp_fib 
  
# Driver Program 
  
print(fibonacci(21))
