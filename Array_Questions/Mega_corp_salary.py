# Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.
# For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
#PSUDOCODE
#take the given array and compare each number to its neighbor, if the number we are testing is larger than one of these, it should have a higher score. 
#FUNC(array)
#take each item in the array, compare it to the +1 & -1 if item > x,y add to their count, 
#else take the +1 as the new number and continue while the array still has numbers to test. 
