#=========Task========
# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
# Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.

# For example, there are n = 7 socks with colors ar = [1, 2, 1, 2, 1, 2, 3]. There is one pair of color 1 and one of color 2. 
# There are three odd socks left, one of each color. The number of pairs is 2.

#=========Solution==========
def sockMerchant(n, ar):
    dictcolor = dict()
    pair = 0

    for i in ar:
        if i not in dictcolor:
            dictcolor[i] = 1
        else:
            dictcolor[i] += 1
    
    for i in dictcolor:
        pair += dictcolor[i] // 2

    return pair

#======Alternative=======
def sockMerchant(n, ar):
    arset = set(ar)
    counter = 0
    pair = 0

    for i in arset:
        for j in ar:
            if i == j:
                counter += 1
        
        pair += counter // 2
        counter = 0
    
    return pair