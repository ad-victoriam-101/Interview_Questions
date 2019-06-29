test_string = "the quick brown fox jumped over the lazy dog12."

def digit_checker(string):
    string = string.replace(" ","")
    all_characters = sorted(string)
    print(all_characters)
print (digit_checker(test_string))