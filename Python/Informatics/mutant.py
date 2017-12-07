N = int(input())

colors = list(map(int, input().split()))

M = int(input())

find = list(map(int, input().split()))

def find_min(num,lst):
    L = 0
    R = len(lst)
    while R>L:
        M = (L+R)//2
        if lst[L] == num:
            return L
        if lst[M] == num:
            if M == L+1:
                return M
            else:
                R = M+1
        elif num < lst[M]:
            R = M
        else:
            L = M+1
    return('NO')

def find_max(num, lst):
    L = 0
    R = len(lst)
    while R>L:
        M = (L+R)//2
        if lst[M] == num:
            if M != len(lst)-1:
                if lst[M+1] != num:
                    return M
            else:
                return M
        if num < lst[M]:
            R = M
        else:
            L = M+1
    return('NO')

for i in find:
    mn = find_min(i,colors)
    mx = find_max(i,colors)
    if mn == 'NO' or mx == 'NO':
        print(0)
    else:
        print(mx-mn+1)
