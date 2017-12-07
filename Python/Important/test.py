def find(q, graf2):
	graf3 = graf2
	i = 0
	while i == 0:
		if len(graf3) == 2:
			i += 1
		else:
			lst = [graf3[0:int(len(graf3)/2)]]
			lst.append(graf3[int(len(graf3)/2):int(len(graf3))])
			if q in lst[0]:
				graf3 = lst[0]
			else:
				graf3 = lst[1]
	return(graf3)

a = input().split()
inter = input().split()
graf1 = []
graf2 = []
i = 0
while i < int(a[1]):
	q = input().split()
	graf1.append(q)
	graf2.append(q[0])
	graf2.append(q[1])
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
	current = used
	graf = []
	answ = 0
	while a == 0:
		j = 0
		while j < len(current):
			if current[j] == find(current[j], graf2)[0]:
				p = []
				p.append(find(current[j], graf2)[1])
				p.append(inter[int(current[j])-1])
				graf.append(p)
				if inter[int(p[0])-1] != '0' and inter[int(p[0])-1] != p[1]:
					a = 1
					answ = 2*step+1
					return(answ)
			else:
				p = []
				p.append(find(current[j], graf2)[0])
				p.append(inter[int(current[j])-1])
				graf.append(p)
				if inter[int(p[0])-1] != '0' and inter[int(p[0])-1] != p[1]:
					a = 1
					answ = (2*step+1)
					return(answ)
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