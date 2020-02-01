# Given a 6 X 6 2D Array, arr:

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in 
# arr's graphical representation:

# a b c
#   d
# e f g

#=======Solution=======
def hourglassSum(arr):
    mx = float('-inf')

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ar = 0
            if j == len(arr)-1 or j == len(arr)-2:
                continue
            if i == len(arr)-1 or i == len(arr)-2:
                continue
            
            ar = arr[i][j] + arr[i][j+1] + arr[i][j+2]+ arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            mx = max(mx, ar)
    
    return mx