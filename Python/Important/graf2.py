a = input().split()
inter = input().split()
graf1 = []
i = 0
while i < int(a[1]):
	q = input().split()
	graf1.append(q)
	i += 1

used = []
i = 0
while i < len(inter):
	if int(inter[i]) != 0:
		used.append(str(i+1))
	i += 1

current = []
NearestNumber = []


def splin():
	i = 0
	step = 0
	a = 0
	g = 0
	p = []
	graf = []
	current = used
	answ = 0
	while a == 0:
		j = 0
		while j < len(current):
			i = 0
			while i < len(graf1):
				if current[j] in graf1[i]:
					if current[j] == graf1[i][0]:
						p = []
						p.append(graf1[i][1])
						p.append(inter[int(current[j])-1])
						graf.append(p)
						if inter[int(p[0])-1] != '0' and inter[int(p[0])-1] != p[1]:
							a = 1
							answ = 2*step+1
							return(answ)
					else:
						p = []
						p.append(graf1[i][0])
						p.append(inter[int(current[j])-1])
						graf.append(p)
						if inter[int(p[0])-1] != '0' and inter[int(p[0])-1] != p[1]:
							a = 1
							answ = (2*step+1)
							return(answ)
				i += 1
			j += 1

		g = 0
		while g < len(graf):
			if inter[int(graf[g][0])-1] != '0':
				if inter[int(graf[g][0])-1] != graf[g][1]:
					answ = (2*step+2)
					return(answ)
			else:
				inter[int(graf[g][0])-1] = graf[g][1]
			g += 1

		current = []

		g = 0
		while g < len(graf):
			if graf[g][0] not in used:
				current.append(graf[g][0])
			g += 1

		graf = []

		step += 1

print(splin())

