NM = input().split()
N = int(NM[0])
M = int(NM[1])

lst = []
i = 0
while i < N:
    lst.append(int(input()))
    i += 1


def find_max(k, lst):
    L = 0
    R = len(lst)
    mx = max(lst)
    while R>L:
        M = (L+R)//2
        num = lst[M]
        if num <= mx:
            cout = 0
            for i in lst:
                cout += i//num
            print(num)
            if cout == k:
                return num
        if num < lst[M]:
            R = M
        else:
            L = M+1
    return('NO')
 
