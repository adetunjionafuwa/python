# -------Task-------
# Read an integer N.
# Without using any string methods, try to print the following:
# 123...N

# Note that "..." represents the values in between.

#-----Solution----------
if __name__ == '__main__':
    n = int(input())

    [print(x + 1, end='') for x in range(n)]

#-------Alternative-------
    for x in range(n):
        print(x + 1, end = '')