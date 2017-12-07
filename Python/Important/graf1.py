

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
# a = [int(x) for x in a]

i = 0
while i < len(a):
	a[i] = int(a[i])
	i += 1

i = 0
while i <len(inter):
	inter[i] = int(inter[i])
	i += 1

used = []
i = 0
while i < len(inter):
	if inter[i] != 0:
		used.append(i+1)
	i += 1

current = []
NearestNumber = []



def splin():
	i = 0
	step = 0
	g = 0
	p = []
	graf = []
	current = used
	answ = 0
	while True:
		j = 0
		while j < len(current):
			i = 0
			for B in graf1[current[j]-1]:
				p = [B, inter[current[j]-1]]
				graf.append(p)
				if inter[p[0]-1] != 0 and inter[p[0]-1] != p[1]:
					answ = 2*step+1
					return(answ)
			j += 1

		g = 0
		while g < len(graf):
			if inter[graf[g][0]-1] != 0:
				if inter[graf[g][0]-1] != graf[g][1]:
					answ = (2*step+2)
					return(answ)
			else:
				inter[graf[g][0]-1] = graf[g][1]
			g += 1

		current = []

		g = 0
		while g < len(graf):
			if graf[g][0] not in used:
				current.append(graf[g][0])
				used.append(graf[g][0])
			g += 1

		graf = []

		step += 1

print(splin())

