# Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.
# For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
#PSUDOCODE
#take the given array and compare each number to its neighbor, if the number we are testing is larger than one of these, it should have a higher score. 
#FUNC(array)
#take each item in the array, compare it to the +1 & -1 if item > x,y add to their count, 
#else take the +1 as the new number and continue while the array still has numbers to test. 
def get_segments(arr):
    #make function that takes an argument
    asc = arr[1] > arr[0]
    prev = arr[0]
    start = 0
    segments = []
    for i, num in enumerate(arr[1:]):
        if (asc and num < prev) or (not asc and num > prev):
            segments.append((asc,i-start +1))
            start = i + 1
            asc = not asc
        prev = num
    segments.append((asc , len(arr)-start))
    return segments

def get_bonuses(arr):
    if not arr:
        return []
    if len(arr) == 1:
        return[1]
    segments = get_segments(arr)
    bonuses = list()
    for segment in segments:
        asc, length = segment
        seg_bonuses = list(range(length))
        if not asc:
            seg_bonuses.reverse()
        bonuses.extend(seg_bonuses)
    bonuses = [x+1 for x in bonuses]
    print(bonuses)
    return bonuses
    
assert get_bonuses([1000])
assert get_bonuses([10,40,200,1000,60,30])