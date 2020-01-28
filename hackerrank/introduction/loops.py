# -----Task------
# Read an integer N. For all non-negative integers i < N, 
# print i^2. See the sample for details.


# -----Solution------

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i**2)


# -----Alternative------
[print(x**2) for x in range(n)]