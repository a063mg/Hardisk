n,H,T = list(map(int,input().split()))

lst = []

mx = H+2

for i in range(n):
	lst.append([])
	h,v = list(map(int,input().split()))
	mx += v
	lst[i].append(h)
	lst[i].append(v)


def check(x,H=H,T=T,lst=lst):
	h = 0
	pas = True
	y = 0
	t = 1
	while t<=T:
		h += x
		for i in lst[::-1]:
			if i[0] <= h:
				if h-i[0]+1 < i[1]:
					h -= h-i[0]+1
				else:
					h -= i[1]
		if h >= H:
			pas = False
			return('YES')
			break
		t += 1

	if pas:
		return('NO')


array = list(range(mx))

L = 0
R = mx
buf = 0
while L<R:
	M = (L+R)//2
	buf = check(array[M])
	if buf == 'NO':
		if M != mx-1:
			if check(array[M+1]) == 'YES':
				print(array[M]+1)
		else:
			print(array[M]+1)
	if buf == 'NO':
		L = M+1
	else:
		R = M


