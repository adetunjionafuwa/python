# -------Task------
# Read two integers and print two lines. The first line should contain integer division,  a//b . 
# The second line should contain float division,  a/b .

# You don't need to perform any rounding or formatting operations.


# -------Solution-------
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)
    print(a / b)

# -------Alternative-------
    print('{0} \n{1}'.format(a // b, a / b))