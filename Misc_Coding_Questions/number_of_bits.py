# Write an algorithm that finds the total number of set bits in all integers between 1 and N.
import math
def bits(n):
    total = 0
    for numb in range(1,n):
        total = total + int((math.log(numb)/math.log(2))+1)
    print(total)
bits(18)