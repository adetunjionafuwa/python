#----------Task----------
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.


#--------Solution----------
if __name__ == '__main__':
    
    n = int(input())

    arrgrade = []
    namearr = []

    for _ in range(n):
        name  = input()
        score = float(input())
        arrgrade.append([name, score])


    
    mnarrgrade = []
    namearr = []

    mn = min([i[:][1] for i in arrgrade])
    for arr in arrgrade:
        if arr[:][1] > mn:
            mnarrgrade.append(arr)

    newmn = min([i[:][1] for i in mnarrgrade])
    for arr in arrgrade:
        if arr[:][1] == newmn:
            namearr.append(arr[:][0])

    namearr.sort()
    [print(x) for x in namearr]