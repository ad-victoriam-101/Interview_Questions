#write a function that teks one parameter named (number), if its even print number //2 and return its value. 
#if odd print and return 3* number +1 

def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number // 2
    elif number % 2 == 1:
        result = 3*number+1
        print(result)
        return result

n = int(input("Please enter a number"))
while n != 1:
    n = collatz(n)
