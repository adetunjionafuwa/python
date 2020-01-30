# ----------Task----------
# Given an integer, , perform the following conditional actions:

# If N is odd, print Weird
# If N is even and in the inclusive range of 2 to 5, print Not Weird
# If N is even and in the inclusive range of 6 to 20, print Weird
# If N is even and greater than 20, print Not Weird


# ----------SOLUTION----------
if __name__ == '__main__':
    N = int(input())

    weird = N % 2 != 0 or N in range(6, 21)

    if weird:
        print('Weird')
    else:
        print('Not Weird')
