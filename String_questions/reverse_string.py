#in this exercise take a given string and reverse it returning the new string and theold one. 
test_string = "the quick brown fox jumped over the lazy dog"
def return_reverse_string(string):
    return "".join(reversed(string))
print return_reverse_string(test_string)
