# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to ,5 print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20 , print Not Weird

def if_odd_weird(n):
    if n%2==0:
        if n in range(2,5):
            print("Not Weird")
        if n in range(6,20):
            print("Weird")
        if n > 20:
            print("Not Weird")
    else:
        print('weird')
        
if_odd_weird(3)
if_odd_weird(16)
if_odd_weird(33)

##############################################################################

check = {True: "Not Weird", False: "Weird"}
#start off by making a dict that checks nothing. 
# then call the print on if it returns true or false 

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])