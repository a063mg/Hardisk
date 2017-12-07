A = input().split()
k = A[0]
del(A[0])
mi = min(A)
mx = max(A)
i = 0
while i < int(k):
	if A[i] == mx:
		A[i] = mi
	i += 1
i = 0
b = ''
while i < len(A):
	b += A[i]
	b += ' '
	i += 1
print(b)