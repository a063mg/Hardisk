p = int(input('p: '))
q = int(input('q: '))

n = p*q
N = (p-1)*(q-1)

e = 0

def nod(a, b):
    return(a%b == 0)

def is_prime(num):
    if num == 2:
        return False
    if num < 2 or num % 2 == 0:
        return False
    for n in list(range(3, int(num**0.5)+2, 2)):
        if num % n == 0:
            return False
    return True

a = list(range(N+1))
a[1] = 0
lst = []

i = 2
while i <= N:
    if a[i] != 0:
        if N%num != 0:
            print(num)
        lst.append(a[i])
    for j in list(range(i, N+1, i)):
        a[j] = 0
    i += 1


def find_special_number(N):
    lst = list(range(n+1))
    for num in lst:
        if is_prime(num):
            if N%num != 0:
                e = num
                return e