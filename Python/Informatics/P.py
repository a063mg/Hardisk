a = input().split()
b = int(a[0])
del(a[0])
i = 0
d = 0
while i < len(a)-2:
	if a[i] == a[i+1] and a[i] == a[i+2]:
		d += 3
		i += 2
	i +