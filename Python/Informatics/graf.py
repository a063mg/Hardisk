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

used = []
i = 0
while i < len(inter):
	if int(inter[i]) != 0:
		used.append(i+1)
	i += 1

current = []
NearestNumber = []

answer = 1e9

Q = used
i = 0
E = [-1]*N
while i < len(Q):
	E[Q[i]-1] = 0
	i += 1
while len(Q) > 0:
	c = Q[0]
	del(Q[0])
	j = 0
	for B in graf1[c-1]:
		if E[B-1] == -1:
			Q.append(B)
			E[B-1] = E[c-1] + 1
			inter[B-1] = inter[c-1]
		elif inter[B-1] != inter[c-1]:
			answer = min(answer, E[B-1]+E[c-1]+1)

print(answer)

