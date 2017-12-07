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