from heapq import heappush


def get_similarity_score(users_a, users_b):
    union = users_a | users_b
    #remember that this is a bitwise or
    intersect = users_a & users_b
    #this is a bitwise and

    return len(intersect) / len(union)
    #returns the division of the two arrays.


def get_similar_websites(visits, k=1):
    #k is the number of pairs, so it will pick the sites that have the most connections. 

    website_users = dict()
    #creates an empty dictionary
    for website, user in visits:
        #for loops can take two arguments in this case it grabs the first (website) then user in visit.
        if website not in website_users:
            #adds the website to the dic if its not in the dic yet
            website_users[website] = set()
            #this makes a set of all unique users to visit a website.
        website_users[website].add(user)

    websites = list(website_users.keys())
    #makes a list from the keys of the div we created earlier. 

    most_similar = list()
    for i in range(len(websites) - 1):
        #jump though all the keys we created in the website list.
        for j in range(i + 1, len(websites)):
            #this will take the keys, compare them to the sim score.Co
            web_a, web_b = websites[i], websites[j]
            sim_score = get_similarity_score(website_users[web_a], website_users[web_b])
            heappush(most_similar, (-sim_score, (web_a, web_b)))
            #remember tha heappush does pretty much what it says
            #it just inserts an element in a 'heap' while maintaining the heap property.

    most_similar = [y for x, y in most_similar]
    #this changes the order of most_similar, for each item in most_similar. 

    return most_similar[:k]


# Tests
visits = [
    ("a", 1),
    ("a", 3),
    ("a", 5),
    ("b", 2),
    ("b", 6),
    ("c", 1),
    ("c", 2),
    ("c", 3),
    ("c", 4),
    ("c", 5),
    ("d", 4),
    ("d", 5),
    ("d", 6),
    ("d", 7),
    ("e", 1),
    ("e", 3),
    ("e", 5),
    ("e", 6),
]
assert get_similar_websites(visits, 1) == [("a", "e")]
assert get_similar_websites(visits, 3) == [("a", "e"), ("a", "c"), ("b", "d")]