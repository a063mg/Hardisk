n = int(input())
lst = input().split()

if len(lst) == 1:
	print(0)
else:
	v =[]

	a = 0
	j = 0
	while j <= len(lst)-1:
		i = 0
		while i <= len(lst)-1:
			if j != i:
				v.append(int(lst[j]))
				v.append(int(lst[i]))
			i += 1
		j += 1

	d = []

	i = 0

	while i < len(v)-1:
		a = v[i]
		b = v[i+1]
		while a != b:
			if a > b:
				a = a - b
			else:
				b = b - a
		d.append(a)
		i += 2

	i = 0
	j = 0
	a = 0
	res = []

	while i < len(d):
		a = 0
		j = 0
		while j < n-1:
			a += d[i] 
			i += 1
			j += 1
		res.append(a)

	print(max(res))
