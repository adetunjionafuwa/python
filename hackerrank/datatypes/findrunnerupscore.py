#----------Task----------
# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the runner-up.

#----------Solution---------
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    #Convert the input map to a python list, then sort
    array = list(arr)
    array.sort()

    #Set the minimum value
    mx = float('-inf')
    mxarr = []
    

    for i in array:
        if i > mx:
            mx = i
            mxarr.append(i)
    mx = mxarr[-2]
        
    print(mx)

#-----------Alternative-----------
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    #Convert the input map to a python set
    setarr = set(list(arr))

    setarr.remove(max(setarr))

    print(max(setarr))

#-------------Alternative----------
#This solution is found to be the most efficient in terms of complexity
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    arr.sort(reverse = True)
    largestNum = arr[0]
    for i in range(n):
        if(arr[i] < largestNum):
            print(arr[i])
            break