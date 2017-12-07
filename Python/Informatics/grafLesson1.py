a = input().split()

b = int(a[0])
a[0] = int(a[1])
a[1] = b 

graf1 = [ [] for i in range(int(a[1])) ]
for i in range(int(a[0])):
	A = input().split()
	A[0] = int(A[0])
	A[1] = int(A[1])
	graf1[A[0] - 1].append(A[1])
	graf1[A[1] - 1].append(A[0])


lsp = []
a = ''
for i in range(len(graf1)):
	a += str(len(graf1[i]))
	a += ' '

print(a)


