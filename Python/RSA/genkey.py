import time

p = int(input('p: '))
q = int(input('q: '))
start = time.time()
print(start)

n = p*q
N = (p-1)*(q-1)

e = 0

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n
        
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in list(range(3, int(num**0.5)+2, 2)):
        if num % n == 0:
            return False
    return True

def nod(a, b):
    return(a%b == 0)

# def find_special_number(n):
#     lst = list(range(n+1))
#     for num in lst:
#         if is_prime(num):
#             if n%num == 0:
#                 e = num
#                 return e

def find_special_number(n):
    a = list(range(n+1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
        for j in list(range(i, n+1, i)):
            a[j] = 0
        i += 1

    del(lst[0])

    for num in lst:
        if n%num != 0:
            e = num
            return e


e = find_special_number(n)

d = mulinv(e, N)

print('Open key: {}, {}'.format(e, n))
print('Closed key: {}, {}'.format(d, n))
