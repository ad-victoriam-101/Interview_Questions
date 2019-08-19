


test_list = ["apple","pleas","please"]
puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
puzzles_list = ["a","e","l","p","s","x","y"]




def check_words(letters,words):
    i = 1
    score = 0
    letters = list(letters)
    for word in words:
        if all(x in set(letters) for x in word) and letters[0] in word:
            #this checks if the word contains any letter from the word and the first letter(aka key letter)
            return 
            #here we have to add a value to a counter to show for that set of letters how many words it can spell. 
            if all(x in set(word) for x in letters):
                #only if the puzzle and the word match exactly aka apple would have to only have a,p,l,e in the test
                print(word,letters)
            else:
                return
        else:
            print("no matching letters and or not matching key letter.")
            return

def spelling_bee_solutions(wordlist,puzzles):
    for puzzle in puzzles:
        puzzle = list(puzzle)
        check_words(puzzle,wordlist)



# check_words(puzzles_list,test_list)

spelling_bee_solutions(test_list,puzzles)

print([sum(set(p) >= set(w) and p[0] in w for w in test_list) for p in puzzles])
