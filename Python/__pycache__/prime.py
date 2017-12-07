def lcs(x, y):
	ans = ''
	lst = []
	i = 0
	while i < len(x):
		if y.find(x[i]) > -1:
			lst.append(x[i])
		i += 1
	lst = list(set(lst))
	lst.sort()
	i = 0
	while i < len(lst):
		ans += lst[i]
		i += 1
	return(ans)

