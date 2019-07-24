import math
import random

def throw_dice(num_dice,faces_of_dice,total_number):
    #determin how many ways its possible to throw N dice with some number of faces to get a specific total. 
    #for example throw_dice(3,6,7) should equal 15
    #psudeo-code. 
    #remember that you can preform Dynamic programing to imporve the On complexity. 
    #create a table to store results of subproblems.
    #one extra row should be used here for simplicity 
    #(number of dice) is directly used as row index andsum is used as column index
    #the entries in the 0th row and 0th column are never used.

    table = [[0]*(total_number+1) for i in range (faces_of_dice+1)]#initialize all entries.
    
    for j in range(1, min (num_dice+1,total_number+1)):
        table[1][j] = 1
        #table entries for only one dice.
    #fill the rest of the entries in table using recursive relation.
    #i: number of dice, j: sum
    for i in range(2, faces_of_dice+1):
        for j in range(1,total_number+1):
            for k in range(1,min(num_dice+1,j)):
                table[i][j]+=table[i-1][j-k]
    # print(dt)
    
    return table[-1][-1]


print(throw_dice(4,2,1))
print(throw_dice(2,2,3))
print(throw_dice(6,3,8))
