a = int(input())
b = int(input())
c = int(input())
d = int(input())

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

pas = 0
step = 0

while pas == 0:
	if a+1 == b:
		if c+1 == d:
			step += c-a
			pas = 1
			print(step)
			break
		else:
			print(0)
			pas = 1
	a += 1
	b += 1
	if b%a == 0:
		b /= int(nod(a,b))
		b = int(b)
		a /= int(nod(a,b))
		a = int(a)
	print(a,b,c,d)
	step += 1


