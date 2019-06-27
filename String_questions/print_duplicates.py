#given a string, print all duplicate characters from a string
test_string = "the quick brown fox jumped over the lazy dog, the quick brown fox jumped over the lazy dog"
fixed_string = "".join(set(test_string))
#this returns a string of all characters sorted alphabetically. !!does not return as is returns a jumbled mess.!!

from collections import OrderedDict
word_fix = "".join(OrderedDict.fromkeys(test_string))
#from keys is super helpful command function. giving a value pair list in responce you can assign anything to a dictionary in python



print fixed_string
print word_fix