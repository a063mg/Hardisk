N = int(input())

lst = []

stek = []

for i in range(N):
	A = list(map(float,input().split()))
	A = A[1:len(A)]
	lst.append(A)

for p in lst:
	i = 0
	stek = []
	while len(p) != 0:
		while p[0] != min(p):
			stek.append(p[0])
			del p[0]
		del p[i]
		pas = 0
		if len(p) != 0:
			if p[0] == min(p):
				pas = 1
				del p[0]
		while pas != 1:
			if len(stek) == 0:
				pas = 1
			elif stek[-1] == min(stek):
				del stek[-1]
			else:
				pas =1
	if len(stek) != 0:
		print(0)
	else:
		print(1)

