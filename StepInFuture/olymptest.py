q = int(input())

r = float(input())

x = 0
x1 = 0
z1 = 0
z = 0
qi = []
ans = 0
mina = 1000

for qi in range(1,q):
	x = int(qi*r)
	x1 = int(qi*r)+1
	z1 = x1/qi
	z = x/qi
	if min(abs(z1-r), abs(z-r)) < mina:
		if abs(z1-r) < abs(z-r):
			mina = abs(z1-r)
			ans = [x1, qi]
		else:
			mina = abs(z-r)
			ans = [x, qi]

print(ans, mina)