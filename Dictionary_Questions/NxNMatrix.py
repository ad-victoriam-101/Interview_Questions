# You are given an N by N matrix of random letters and a dictionary of words. Find the maximum number of 
# words that can be packed on the board from the given dictionary.

# A word is considered to be able to be packed on the board if:

# It can be found in the dictionary
# It can be constructed from untaken letters by other words found so far on the board
# The letters are adjacent to each other (vertically and horizontally, not diagonally).
# Each tile can be visited only once by any word.

# For example, given the following dictionary:

# { 'eat', 'rain', 'in', 'rat' }
# and matrix:

# [['e', 'a', 'n'],
#  ['t', 't', 'i'],
#  ['a', 'r', 'a']]
givenDictionary = { 'eat', 'rain', 'in', 'rat' }
givenMatrix = [['e', 'a', 'n'],
               ['t', 't', 'i'],
               ['a', 'r', 'a']]
