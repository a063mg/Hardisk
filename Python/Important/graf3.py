a = input().split()
N = int(a[0])
inter = input().split()
graf1 = []
for i in range(N): graf1.append([])
i = 0
while i < int(a[1]):
	q = input().split()
	A = int(q[0])
	B = int(q[1])
	graf1[A-1].append(B)
	graf1[B-1].append(A)
	i += 1

i = 0
Q = []
U = [-1]*N
Q.append(1)
step = 0
while len(Q) > 0:
	c = Q[0]-1
	for r in graf1[c]:
		if U[r-1] == -1:
			U[r-1] = U[c]+1
			Q.append(r)
	del(Q[0]) 