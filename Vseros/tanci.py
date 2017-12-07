N = int(input())

lst = [[]]

j = 0
for i in range(N):
	if i%2 == 0 and i != 0:
		lst.append([])
		j += 1
	lst[j].append(i+1)
	