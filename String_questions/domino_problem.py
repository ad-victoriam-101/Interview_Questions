#You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

# L, meaning the domino has just been pushed to the left,
# R, meaning the domino has just been pushed to the right, or
# ., meaning the domino is standing still.
# Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

# For example, given the string .L.R....L, you should return LL.RRRLLL.

# Given the string ..R...L.L, you should return ..RR.LLLL.

test_string = ".L.R....L"
class Solution(object):
    def domino_fall(self,string_dominos):
        symbols = [(i,x) for i, x in enumerate(string_dominos) if x != "."]
        #take given string and count through it, keeping only L,R's 
        symbols = [(-1,"L")]+symbols+[(len(string_dominos),"R")]
        #black magic i guess.
        ans = list(string_dominos)
        for (i,x),(j,y) in zip(symbols,symbols[1:]):
            if x == y:
                for k in xrange(i+1,j):
                    ans[k] = x
            elif x > y:
                for k in xrange(i+1,j):
                    ans[k] = ".LR"[cmp(k-i,j-k)]
        return "".join(ans)



#too hard i'm a dumb bitch coppied from the internet