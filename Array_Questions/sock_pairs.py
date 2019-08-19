#given an array of ints representing pairs of socks, determine how many pairs of socks you can make. 
#info given is the length of the arry, N and the array arr = [1,2,1,2,1,3,2]
arr = [1,2,1,2,3,2]
n = len(arr)
import math as mt 
from itertools import groupby
def count_pairs(arr,n):
    mp = dict()
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]]=1
    ans = 0
    for it in mp:
        count = mp[it]
        ans += (count * (count-1))//2
    return ans
#this is not exactly right, this counts every pair and will count doubles. 
# print(count_pairs(arr,n))
print(arr, n)
count_of_pairs = map(int,raw_input().split())

pairs = 0
for val in [len(list(group)) for key , group in groupby(sorted(count_of_pairs))]:
    pairs = pairs + val/2
return pairs

