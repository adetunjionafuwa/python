#==========Task==========
# Given an array 'a' of 'n' integers and a number, 'd', perform 'd' left rotations on the array. 
# Return the updated array to be printed as a single line of space-separated integers.

#=========Solution=========
def rotLeft(a, d):
    leftshift = d % len(a)
    return a[leftshift:] + a[:leftshift]

#==========Alternative===========
def rotLeft(a, d):
    arr = []
    for i in range(len(a)):
        arr.append(a[(i+d)%len(a)])
    return arr