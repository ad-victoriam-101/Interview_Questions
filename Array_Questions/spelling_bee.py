#this is a coding question asked by dropbox, we don't know exactly what they are asking so this is some guesses on what that could be. 
#guess one 
#given a word, users will attempt to spell it, if they are right it returns true, If they are close, (within 2 letters) tell them that, if they are super far off return false. 
my_list = ["apple","pleas","please"]
puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
# new_list = []
for word in puzzles:
    new_list = (list(dict.fromkeys(word)))
#newlist == charSet
print(new_list)

def char_count(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i,0)+1
    print(dict)
    return dict
def possible_words(lwords,new_list):
    for word in lwords:
        flag = 1
        chars = char_count(word)
        for key in chars:
            if key not in new_list:
                flag = 0
            else:
                if new_list.count(key) != chars[key]:
                    flag = 0
            if flag == 1:
                print(word)
possible_words(my_list,new_list)




























##############################################################################################################################################
# for word in my_list:
#     new_list.append(list(dict.fromkeys(word)))
# for letters in new_list:
#     print(new_list)
# def spelling_bee_solutions(wordlist,puzzles):
#     sorted_list = []
#     for word in wordlist:
#         sorted(word)
#         sorted_list.append(list(dict.fromkeys(word)))
#     print(sorted_list)
#     for puzzle in puzzles:
#         for let in puzzle:
#             i = 0
#             while i < (len(puzzle)):
#                 if let in sorted_list[i]:
#                     print(let,sorted_list[i])
#                 i+=1
#         print(puzzle)

# spelling_bee_solutions(my_list,puzzles)






#guess two
#users are asked to spell a word, (akin to hangman style.) if they get a certain amount wrong game over. else return victory. 


#guess three
#given a random word, give the user the number of letters and it being used in a sentence or definition. 