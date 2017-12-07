N = int(input())
K = int(input())

def nod(a,b):
	if b == a or b == 0:
		return b
	if a == 0:
		return b
	while a != 0 and b != 0:
		if a > b:
			a = a%b
		else:
			b = b%a
	return a + b 

okrug = int(N/2)+1
region = int(K/2)+1

print(okrug*region)
