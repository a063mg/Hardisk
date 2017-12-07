p = int(input('p: '))
q = int(input('q: '))

n = p*q
N = (p-1)*(q-1)

e = 0 

a = list(range(n+1))
a[1] = 0
lst = [1]

def nod(a, b):
	return(a%b == 0)

i = 2
while i <= N:
	if a[i] != 0:
		if nod(N, a[i]) == False:
			e = a[i]
			break;
	for j in list(range(i, n+1, i)):
		a[j] = 0
	i += 1

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

d = mulinv(e, N)

print('Open key: {}, {}'.format(e, n))
print('Closed key: {}, {}'.format(d, n))

dic = {'a': 5608, 'b': 8697, 'c': 6763, 'd': 9015, 'e': 8518, 'f': 6424, 'g': 3263, 'h': 2487, 'i': 4256, 'j': 6204, 'k': 6384, 'l': 3637, 'm': 4301, 'n': 6809, 'o': 2989, 'p': 3907, 'q': 7634, 'r': 2000, 's': 1640, 't': 7129, 'u': 1625, 'v': 8037, 'w': 6739, 'x': 1544, 'y': 5289, 'z': 6998, 'A': 6799, 'B': 4650, 'C': 9588, 'D': 4503, 'E': 7247, 'F': 6352, 'G': 6522, 'H': 5753, 'I': 7611, 'J': 6518, 'K': 6023, 'L': 1950, 'M': 5107, 'N': 7884, 'O': 9262, 'P': 8416, 'Q': 3773, 'R': 8239, 'S': 7607, 'T': 9348, 'U': 5655, 'V': 1046, 'W': 2990, 'X': 1557, 'Y': 7029, 'Z': 9326, '1': 6681, '2': 1208, '3': 8196, '4': 2481, '5': 5420, '6': 9723, '7': 5780, '8': 2734, '9': 9129, '0': 4722}

text = str(input('Enter your word: '))
b = ''

for i in range(len(text)):
	b += str(dic[text[i]])

ret = ''
i = 0
while i < len(b):
	m = int(str(b)[i:i+4])
	encode = (m**e)%n
	ret += str(encode)
	ret += ' '
	i += 4

print(ret)



