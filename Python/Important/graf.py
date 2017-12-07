a = input().split()
inter = input().split()
graf = []
graf1 = []
graf2 = []
i = 0
while i < int(a[1]):
	q = input().split()
	graf.append(q[0])
	graf.append(q[1])
	if (q[0] in graf2) == False:
		graf2.append(q[0])
	if (q[1] in graf2) == False:
		graf2.append(q[1])
	graf1.append(q)
	i += 1

i = 0
j = 1
res = []
vil = []
while j < len(graf):
 	if int(inter[int(graf[i])-1]) != 0 and int(inter[int(graf[j])-1]) != 0 and int(inter[int(graf[i])-1]) != int(inter[int(graf[j])-1]):
 		res.append(graf[i])
 		res.append(graf[j])
 	j += 1


def sort(q):
	lst = []
	i = 0
	while i < len(graf1):
		if graf1[i][0] == q:
			lst.append(graf1[i][1])
		else:
			if graf1[i][1] == q:
				lst.append(graf1[i][0])
		i += 1
	return(lst)

used = []
index = []
a = 0
b = 0
used.append(res[0])
while a == 0:
	q = sort(used[len(used)-1])
	i = 0
	while i < len(q):
		if (q[i] in used) != True:
			index.append(q[i])
		i += 1
	i = 0
	while i < len(index):
		if (index[i] in used) != True:
			used.append(index[i])
		i += 1
	if res[1] in index:
		a = 1
	index = []
	b += 1
print(b)
	
