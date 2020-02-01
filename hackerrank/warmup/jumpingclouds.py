def jumpingOnClouds(c):
    counter = 0
    zerostate = 0

    for i in c:
        if i == 0:
            zerostate += 1
        if i == 1:
            if zerostate > 2:
                #Keeping track of the chain of zero in the array.
                #The pattern shows that the following formular works for 0's > 2
                #Else we can increment counter by 1 0r 2
                counter += (zerostate // 2) + 1
            else:
                counter += zerostate
            zerostate = 0
    
    if zerostate > 2:
        counter += (zerostate // 2) + 1
    else:
        counter += zerostate
        
    return counter - 1