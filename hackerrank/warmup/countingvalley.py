def countingValleys(n, s):
    floor = 0
    valleycount = 0
    for i in s:
        if i == 'D':
            floor += 1
        else:
            floor -= 1
        if floor == 0 and i == 'U':
            valleycount += 1
    return valleycount