Lst = input().split()
N = int(Lst[0])
K = int(Lst[1])
S = int(Lst[2])

lst = [[ 0 for j in range(K)] for i in range(K)]

i = 0
c = 0
for j in range(K):
	i = 0
	while i < K:
		if c < S:
			lst[j][i] = 1
			c += 1
		else:
			lst[j][i] = 0
		i += 1



for j in range(N):
	lst1 = ''
	for i in range(N):
		lst1 += str(lst[j%K][i%K]) 
		lst1 += ' '
	print(lst1)