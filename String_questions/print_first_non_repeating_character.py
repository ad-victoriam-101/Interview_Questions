#print th efirst non-repeating character. 
no_of_char = 256
index = 0
#returns an array of 256 containers
def get_char_count_array(string):
    count = [0]*no_of_char
    for i in string:
        count[ord(i)]+= 1
        return count
def first_Non_repeating(string):
    count = get_char_count_array(string)
    index = -1
    k = 0
    for i in string: 
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
        return index
string = "geeksforgeeks"
dex = first_Non_repeating(string)
if index == 1: 
    print ("all characters are repeating or string is empty.")
else:
    print ("first non repeating character is: " +string[index])
 