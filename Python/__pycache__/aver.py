def sort(a, b):
	c = a + b
	d = ''
	a = 1
	i = 0
	while a != 0:
		a = 0
		i = 0
		while i < len(c)-1:
			if c[i] > c[i+1]:
				d = c[i]
				c[i] = c[i+1]
				c[i+1] = d
				a = 1
			i += 1
	print(c)
