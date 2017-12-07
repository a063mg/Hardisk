inp = list(map(int, input().split()))

n = inp[0] 
m = inp[1] 

al = []

def clone(lsit):
	lst = []
	for i in range(len(lsit)):
		lst.append([])
		for j in lsit[i]:
			lst[i].append(j)
	return lst

graf1 = [ [] for i in range(m) ]

i = 0

while i < m:
	q = input().split()
	A = int(q[0])
	B = int(q[1])
	graf1[A-1].append(B)
	graf1[B-1].append(A)
	i += 1

lsit = []
lsit = clone(graf1)

for j in range(len(lsit)):
	for i in range(len(lsit[j])):
		lst = []
		lst = clone(graf1)
		del lst[j][i]
		Q = [1]
		used = [1]
		while Q != []:
			for i in lst[Q[0]-1]:
				if i not in used:
					Q.append(i)
					used.append(i)
			del Q[0]
		print(used, lst)




