#Every positive fraction can be represented as sum of unique unit fractions. A fraction is unit fraction if numerator is 1 and denominator is a positive integer, for example 1/3 is a unit fraction. Such a representation is called Egyptian Fraction as it was used by ancient Egyptians.
#given a fraction, give the returning egyptian fraction. 
import math
#importing math package to use the ceiling function.
def egyptian_fraction(numerator,denominator):
    print("the egyptian Fraction"+ "representation of {0}/{1} is ".format(numerator,denominator))

    #first create an empty list to store the denominator.
    empty_list = []
    #create a while loop that will slowly whittle down the fraction untill it become 0
    while numerator != 0:
        #then take the ceiling of this particular fraction.
        x = math.ceil(denominator/numerator)
        print(x)
        empty_list.append(x)
        numerator = x * numerator - denominator
        denominator = denominator*  x
    for i in range(len(empty_list)):
        if i != len(empty_list)-1:
            print("1/{0} + ".format(empty_list[i]))
        else:
            print("1/{0}".format(empty_list[i]))
egyptian_fraction(6,14)
numer = input("what fraction would you like to see the egyptian fraction for? ")
denom = input("denomenator also.")
int(denom)
int(numer)
egyptian_fraction(numer,denom)