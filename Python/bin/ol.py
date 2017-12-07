N = int(input())

graf = [ [] for i in range(N ) ]
road = [ [] for i in range(N ) ]

for i in range(N):
	lst = list(map(int,input().split()))
	for j in range(len(lst)):
		if lst[j] != 0:
			road[i].append(lst[j])
			graf[i].append(j+1)

vays = list(map(int,input().split()))

lenth = 0

for i in range(len(vays)-1):
	if vays[i+1] in graf[vays[i]-1]:
		for j in range(len(graf[vays[i]-1])):
			if vays[i+1] == graf[vays[i]-1][j]:
				lenth += road[vays[i]-1][j]

print(lenth)