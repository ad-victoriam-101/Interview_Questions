# given a string, find the length of the smallest window thatcontains every distinct character. Characters may appear more than once in the indow. 
# for example , given {jiujistu} you should return 5 corresponding to the final 5 letters. 
from collections import defaultdict
#new sorted dicts maintain their sort order, 
string = "jiujitsu"
max_char = 256
def window_words(string):
    n = len(string)
    #count all distinct characters
    distint_count = len(set([x for x in string]))
    count,start,start_index,min_len = 0,0,-1,9999999999
    current_count = defaultdict(lambda: 0)
    for j in range(n):
        current_count[string[j]]+=1

        if current_count[string[j]] == 1:
            count += 1
        if count == distint_count:
            while current_count[string[start]]>1:
                if current_count[string[start]]>1:
                    current_count[string[start]]-=1
                start +=1
            length_window = j - start + 1
            if min_len > length_window:
                start_index = start
    return string[start_index: start_index+min_len]

if __name__ =='__main__':
    print("smallest window containing all distinct characters is {}".format(window_words("aabcbcdbca")))


