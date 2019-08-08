from heapq import heappush

def similarrity_score(user_one,user_two):
    union_check = user_one or user_two
    intersection = user_one and user_two

    return len(intersection)/len(union_check)

def similarity_websites(visits, k = 1):
    website_users = dict()
    for website, user in visits:
        if website not in website_users:
            website_users[website] = set()
        website_users[website].add(user)
    websites = list(website_users.keys())

    most_similar = list()
    for i in range(len(website)-1):
        for j in range(i + 1, len(website))