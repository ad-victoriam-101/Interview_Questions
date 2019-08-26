def counting_valleys(n,s):
    alt = 0
    num_valley = 0
    for char in s:
        if char == "U":
            if alt == -1:
                num_valley += 1
            alt += 1
        else:
            alt -= 1


