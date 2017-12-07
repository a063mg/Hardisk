from collections import Counter

def reverse(num):
	return(num[::-1])
	
def fast_pow(num,n):
	c = 1
	while n:
		if n%2==0:
			n /= 2
			num *=num
		else:
			n -= 1
			c *= num
	return(c) 

def fast_mod_pow(x, n, m):
  count=1;
  if not n:
    return 1
  while n:
    if n%2==0:
      n /= 2;
      x*=x;
      x %= m;
    else:
      n -= 1;
      count*=x;
      count %=m;
  return count % m

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in list(range(3, int(num**0.5)+2, 2)):
        if num % n == 0:
            return False
    return True

def ifint(integer):
    integer = str(integer)
    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if integer == '':
         return False
    else:
        ifinteger = True
        for i in range(len(integer)):
            if integer[i] not in lst:
                ifinteger = False
        return(ifinteger)

def double(lst):
	counter = {}	
	for elem in lst:
		counter[elem] = counter.get(elem, 0) + 1
	doubles = {element: count for element, count in counter.items() if count > 1}
	return(counter)

def nod(a,b):
    while a != 0 and b!= 0:
    	if a > b:
    		a = a%b
    	else:
    		b =b%a
    return(a+b)

def factor(n):
    Ans = ''
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans+= str(d)
            Ans += ' '
            n //= d
        else:
            d += 1
    if n > 1:
        Ans+=str(n)
        Ans += ' '
    return Ans


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