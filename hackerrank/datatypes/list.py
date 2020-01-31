if __name__ == '__main__':
    N = int(input())
    arr = []
    
    num = 0
    for i in range(N):
        n = input().split(' ')
        if n[0] == 'insert':
            arr.insert(int(n[1]), int(n[2]))
        elif n[0] == 'print':
            print(arr)
        elif n[0] == 'append':
            arr.append(int(n[1]))
        elif n[0] == 'remove':
            arr.remove(int(n[1]))
        elif n[0] == 'sort':
            arr.sort()
        elif n[0] == 'reverse':
            arr.reverse()
        elif n[0] == 'pop':
            arr.pop()