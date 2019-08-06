#a regular number in mathematics is defined as one which evenly divides some power of 60.
#given an integer N write a program that returns in order, the first N regular numbers. 
def is_hamming_nums(x):
    if x ==1 :
        return 1
    if x % 2 == 0:
        return is_hamming_nums(x/2)
    if x % 3 == 0:
        return is_hamming_nums(x/3)
    if x % 5 == 0 :
        return is_hamming_nums(x/5)
    return 0

def hamming_sequence(x):
    if x == 1:
        return 1
    hamming_sequence(x-1)
    if is_hamming_nums(x) == True:
        print("%s" % x)
print(is_hamming_nums(7))
print(is_hamming_nums(1))
hamming_sequence(24)
