N = int(input())

lst = [ [] for i in range(N)]

for i in range(N):
	a,b = map(int, input().split())
	lst[a-1].append(b)
	lst[b-1].append(a)

used = []

lst = [[3,4,5],[4,5,6],[1,6,4],[1,2,3],[1,2,6],[2,3,5]]

Q = [1,lst[0][0],lst[0][1],lst[0][2]]


for i in range(len(Q)):
	for k in range(len(Q)):
		j = lst[Q[k]-1]
		pas = True
		if Q[i] not in j and Q[i] != Q[k]: 
			print(Q[i],j)


