test_list = ["apple","pleas","please"]
puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]


def spellingBeeSolutions(wordlist, puzzles):
    #maping the word sets to a list helps, It also removes the duplicate letters. 
    word_sets = list(map(set, wordlist))
    # print(word_sets)
    solved_arr = [sum(word.issubset(puzzle) and puzzle[0] in word for word in word_sets) for puzzle in puzzles]
    #Set A is said to be the subset of set B if all elements of A are in B.(python documentation) 
    #rembmber that puzzle[0] is the key letter and has to be in the subset. if not the code should skip it.(this seems to be a slow down as its checking words with out it) 
    #for puzzle in puzzles will check that 1.) every word has the keyword, and that it contains all other letters in the word. 
    # for words in word_sets:
    #     if all(x in set(puzzle)for x in words)and puzzle[0] in words:
    #         print(words,puzzle)
    print(solved_arr)
    return(solved_arr)
    
def beespelling(wordlist,puzzles):
    word_sets = list(map(set, wordlist))
    for puzzle in puzzles:
        solved_arr = [sum(word.issubset(puzzle) and puzzle[0] in word for word in word_sets) for puzzle in puzzles]
        print(solved_arr)
        return(solved_arr)
spellingBeeSolutions(test_list,puzzles)

beespelling(test_list,puzzles)