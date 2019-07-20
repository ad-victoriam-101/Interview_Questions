#A step word is formed by taking a given word, adding a letter, 
#and anagramming the result. For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".
#Given a dictionary of words and an input word, create a function that returns all valid step words.
#Codeblock Start
##############################################################################
#step 1 is to take said string and sort it so the letters are alphabetical.
#step 2 is to then add each letter of the alphabet individually, check that new word against the dictionary of sorted words
#step 3 if the new letter can create a new word add said new word to a list, 
#repeat steps until all letters of alphabet are tested. return the list. 
import string

alphabet = list(string.ascii_lowercase)
#learned how to dothis  as opposed to coding out each letter.
print (alphabet)
step_words_checked = []
def step_word_anagram(string,dictionary_words):
    sorted_string = sorted(string)
    print(sorted_string)
    count = 0
    for letter in alphabet:
        step_word = sorted_string + alphabet[count]
        for word in dictionary_words:
            step_dic = sorted(dictionary_words[count])
            if step_word == step_dic:
                step_words_checked.append(step_dic)




