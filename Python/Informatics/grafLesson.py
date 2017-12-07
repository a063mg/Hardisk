a = input().split()


graf1 = [ [] for i in range(int(a[0])) ]
for i in range(int(a[0])):
	A = input().split()
	A[0] = int(A[0])
	A[1] = int(A[1])
	graf1[A[0] - 1].append(A[1])
	graf1[A[1] - 1].append(A[0])

B = input().split()
B[0] = int(B[0])
B[1] = int(B[1])

# for i in len(graf[B[0]-1]):
# 	graf[B[0]-1][i]

pas = 0
cout = 0

Q = [B[0]]
Ex = [B[0]]

def G(num):
	for i in range(len(num)):
		if num[i] != B[1]:
			if num[i] not in Ex:
				Q.append(num[i])
				Ex.append(num[i])
		else:
			return(1)

	return(0)
# for i in range(len(graf1[B[0]-1])):
# 	for k in range(len(graf1[B[0]-1])):
# 		if graf1[B[0]-1][k] != B[1]:
# 			Q.append(graf1[B[0]-1][k])
# 		else:
# 			break
# 	for j in len(graf1[B[0]-1][i]):

# G(graf1[Q[0]-1])
# del Q[0]

# C = Q
# for i in range(len(C)):
# 	G(graf1[C[i]-1])
while pas == 0:
	pas = G(graf1[Q[0]-1])
	del Q[0]
	cout += 1


