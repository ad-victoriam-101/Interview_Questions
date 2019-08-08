from heapq import heappush

def similarrity_score(user_one,user_two):
    union_check = user_one or user_two
    intersection = user_one and user_two