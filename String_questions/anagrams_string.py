#given two strings check if they are anagrams of eachother. 
#inthis it doesn't matter if the two strings are words or in the same order, Only that they contain the same letters. 
anagram_1 = "dirty room"
anagram_2 = "dormitory"

def test_anagram(word_one,word_two):
    word_one = word_one.replace(" ","")
    word_two = word_two.replace(" ","")
    string_one = "".join(set(word_one))
    string_two = "".join(set(word_two))
    print(string_one,string_two)
    if string_one == string_two:
        print("the two words are anagrams")
    elif string_one != string_two:
            print("the words aren't anagrams")

test_anagram(anagram_1,anagram_2)

#found a better way todo this online. the faster way is. 

# function to check if two strings are 
# anagram or not  
def check(s1, s2): 
      
    # the sorted strings are checked using python built in sort method which returns a sorted list that doesn't effect the orinal. 
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")          
          
# driver code   
s1 ="listen"
s2 ="silent" 
check(s1, s2) 