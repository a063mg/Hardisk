lst = list(map(int,input().split()))

lst.sort()

t1 = 0
t2 = 0
f = 0
for i in lst[::-1]:
	if t1 > t2:
		f += 1
		t2 += i
	else:
		t1 += i


if t1 == t2 and f == 3:
	print('YES')
else:
	print('NO')