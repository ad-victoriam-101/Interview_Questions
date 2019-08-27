# Complete the repeatedString function in the editor below. 
# It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider

s = "a"
n = 1000000000000
def repeat_to_length(string_to_expand, length):
    if s == 'a':
        return n
    else:
        shortend_string = (string_to_expand * (int(length/len(string_to_expand))+1))[:length]
        return shortend_string.count('a')



print(repeat_to_length(s,n))

