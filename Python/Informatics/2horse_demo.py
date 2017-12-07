cor = input()

cord1 = cor[0:2]

cord2 = cor[3:5]

dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h':8}

cord1 = [dic[cord1[0]], int(cord1[1])]

cord2 = [dic[cord2[0]], int(cord2[1])]

pas = 0

if ((cord1[0] % 2 == 0) and (cord1[1] % 2 != 0)) or ((cord1[0] % 2 != 0) and (cord1[1] % 2 == 0)):
	if ((cord2[0] % 2 == 0) and (cord2[1] % 2 == 0)) or ((cord2[0] % 2 != 0) and (cord2[1] % 2 != 0)):
		print(-1)
		pas = 1
elif ((cord2[0] % 2 == 0) and (cord2[1] % 2 != 0)) or ((cord2[0] % 2 != 0) and (cord2[1] % 2 == 0)):
	if ((cord1[0] % 2 == 0) and (cord1[1] % 2 == 0)) or ((cord1[0] % 2 != 0) and (cord1[1] % 2 != 0)):
		print(-1)
		pas = 1

if pas == 0:
	Used1 = [cord1]
	Used = [cord2]

	Q1 = [[cord1]]
	Q = [[cord2]]

	k = 0
	k1 = 0

	step = 0

	def upload1(cor1):
		pos = [0, 0]
		pos[0] = cor1[0] + 1 
		pos[1] = cor1[1] + 2
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
			Q[j].append(pos)
			Used.append(pos)

		pos = [0, 0]
		pos[0] = cor1[0] + 1 
		pos[1] = cor1[1] - 2
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
			Q[j].append(pos)
			Used.append(pos)
		pos = [0, 0]
		pos[0] = cor1[0] - 1 
		pos[1] = cor1[1] + 2
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
			Q[j].append(pos)
			Used.append(pos)

		pos = [0, 0]
		pos[0] = cor1[0] - 1 
		pos[1] = cor1[1] - 2
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
			Q[j].append(pos)
			Used.append(pos)

		pos = [0, 0]
		pos[0] = cor1[0] + 2 
		pos[1] = cor1[1] + 1
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
			Q[j].append(pos)
			Used.append(pos)

		pos = [0, 0]
		pos[0] = cor1[0] + 2 
		pos[1] = cor1[1] - 1
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
			Q[j].append(pos)
			Used.append(pos)

		pos = [0, 0]
		pos[0] = cor1[0] - 2 
		pos[1] = cor1[1] + 1
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
			Q[j].append(pos)
			Used.append(pos)

		pos = [0, 0] 
		pos[0] = cor1[0] - 2 
		pos[1] = cor1[1] - 1
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
			Q[j].append(pos)
			Used.append(pos)

		return(0)





	def upload2(cor1, cor2):
		global ans
		pos = [0, 0]
		pos[0] = cor1[0] + 1 
		pos[1] = cor1[1] + 2
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
					
			if pos not in cor2:
				Q1[j1].append(pos)
				Used1.append(pos)
			else:
				Q1[j1].append(pos)
				Used1.append(pos)
				ans = pos
				return(1)

		pos = [0, 0]
		pos[0] = cor1[0] + 1 
		pos[1] = cor1[1] - 2
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
					
			if pos not in cor2:
				Q1[j1].append(pos)
				Used1.append(pos)
			else:
				ans = pos
				Q1[j1].append(pos)
				Used1.append(pos)
				return(1)
		pos = [0, 0]
		pos[0] = cor1[0] - 1 
		pos[1] = cor1[1] + 2
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
					
			if pos != cor2:
				Q1[j1].append(pos)
				Used1.append(pos)

			else:
				Q1[j1].append(pos)
				Used1.append(pos)
				ans = pos
				return(1)

		pos = [0, 0]
		pos[0] = cor1[0] - 1 
		pos[1] = cor1[1] - 2
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
					
			if pos not in cor2:
				Q1[j1].append(pos)
				Used1.append(pos)
			else:
				Q1[j1].append(pos)
				Used1.append(pos)
				ans = pos
				return(1)
		pos = [0, 0]
		pos[0] = cor1[0] + 2 
		pos[1] = cor1[1] + 1
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
					
			if pos not in cor2:
				Q1[j1].append(pos)
				Used1.append(pos)

			else:
				Q1[j1].append(pos)
				Used1.append(pos)
				ans = pos
				return(1)

		pos = [0, 0]
		pos[0] = cor1[0] + 2 
		pos[1] = cor1[1] - 1
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
					
			if pos not in cor2:
				Q1[j1].append(pos)
				Used1.append(pos)
			else:
				Q1[j1].append(pos)
				Used1.append(pos)
				ans = pos
				return(1)

		pos = [0, 0]
		pos[0] = cor1[0] - 2 
		pos[1] = cor1[1] + 1
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
					
			if pos not in cor2:
				Q1[j1].append(pos)
				Used1.append(pos)

			else:
				Q1[j1].append(pos)
				Used1.append(pos)
				ans = pos
				return(1)

		pos = [0, 0] 
		pos[0] = cor1[0] - 2 
		pos[1] = cor1[1] - 1
		if not((pos[0] > 8 or pos[0] < 1)) and not((pos[1] > 8 or pos[1] < 1)):
					
			if pos not in cor2:
				Q1[j1].append(pos)
				Used1.append(pos)
			else:
				Q1[j1].append(pos)
				Used1.append(pos)
				ans = pos
				return(1)

		return(0)


	j = 1
	j1 = 1
	a = 0
	b = 0

	while a == 0:
		Q.append([])
		Q1.append([])

		for i in range(len(Q[k])):
			b = upload1(Q[k][i])

		for i in range(len(Q1[k1])):
			a = upload2(Q1[k1][i], Q[j])
			if a == 1:
				print(k1+1)
				break;

		j1 += 1
		k1 += 1
		j += 1
		k += 1









