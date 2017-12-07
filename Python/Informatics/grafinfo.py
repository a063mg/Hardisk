A = input().split()

dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

xy1 = [dic[A[0][0]], int(A[0][1])]
xy2 = [dic[A[1][0]], int(A[1][1])]

Q = [[xy1]]
a = 0
dont = [xy1]

def refresh(cur_xy):
	if (cur_xy[0] + 1 <= N) and (cur_xy[1] + 2 <= N) and ([cur_xy[0] + 1, cur_xy[1] + 2] not in lst):
		if ([cur_xy[0] + 1, cur_xy[1] + 2] != buf[j]):
			loc.append([cur_xy[0] + 1, cur_xy[1] + 2])
			lst.append([cur_xy[0] + 1, cur_xy[1] + 2])
		else:
			loc.append([cur_xy[0] + 1, cur_xy[1] + 2])
			lst.append([cur_xy[0] + 1, cur_xy[1] + 2])
			buf.append(cur_xy)
			return(1)
	if (cur_xy[0] - 1 > 0) and (cur_xy[1] + 2 <= N) and ([cur_xy[0] - 1, cur_xy[1] + 2] not in lst):
		if ([cur_xy[0] - 1, cur_xy[1] + 2] != buf[j]):
			loc.append([cur_xy[0] - 1, cur_xy[1] + 2])
			lst.append([cur_xy[0] - 1, cur_xy[1] + 2])
		else:
			loc.append([cur_xy[0] - 1, cur_xy[1] + 2])
			lst.append([cur_xy[0] - 1, cur_xy[1] + 2])
			buf.append(cur_xy)
			return(1)
	if (cur_xy[0] + 1 <= N) and (cur_xy[1] - 2 > 0) and ([cur_xy[0] + 1, cur_xy[1] - 2] not in lst):
		if ([cur_xy[0] + 1, cur_xy[1] - 2] != buf[j]):
			loc.append([cur_xy[0] + 1, cur_xy[1] - 2])
			lst.append([cur_xy[0] + 1, cur_xy[1] - 2])
		else:
			loc.append([cur_xy[0] + 1, cur_xy[1] - 2])
			lst.append([cur_xy[0] + 1, cur_xy[1] - 2])
			buf.append(cur_xy)
			return(1)
	if (cur_xy[0] - 1 > 0) and (cur_xy[1] - 2 > 0) and ([cur_xy[0] - 1, cur_xy[1] - 2] not in lst):
		if ([cur_xy[0] - 1, cur_xy[1] - 2] != buf[j]):
			loc.append([cur_xy[0] - 1, cur_xy[1] - 2])
			lst.append([cur_xy[0] - 1, cur_xy[1] - 2])
		else:
			loc.append([cur_xy[0] - 1, cur_xy[1] - 2])
			lst.append([cur_xy[0] - 1, cur_xy[1] - 2])
			buf.append(cur_xy)
			return(1)
	if (cur_xy[0] + 2 <= N) and (cur_xy[1] + 1 <= N) and ([cur_xy[0] + 2, cur_xy[1] + 1] not in lst):
		if ([cur_xy[0] + 2, cur_xy[1] + 1] != buf[j]):
			loc.append([cur_xy[0] + 2, cur_xy[1] + 1])
			lst.append([cur_xy[0] + 2, cur_xy[1] + 1])
		else:
			loc.append([cur_xy[0] + 2, cur_xy[1] + 1])
			lst.append([cur_xy[0] + 2, cur_xy[1] + 1])
			buf.append(cur_xy)
			return(1)
	if (cur_xy[0] - 2 > 0) and (cur_xy[1] + 1 <= N) and ([cur_xy[0] - 2, cur_xy[1] + 1] not in lst):
		if ([cur_xy[0] - 2, cur_xy[1] + 1] != buf[j]):	
			loc.append([cur_xy[0] - 2, cur_xy[1] + 1])
			lst.append([cur_xy[0] - 2, cur_xy[1] + 1])
		else:
			loc.append([cur_xy[0] - 2, cur_xy[1] + 1])
			lst.append([cur_xy[0] - 2, cur_xy[1] + 1])
			buf.append(cur_xy)
			return(1)
	if (cur_xy[0] + 2 <= N) and (cur_xy[1] - 1 > 0) and ([cur_xy[0] + 2, cur_xy[1] - 1] not in lst):
		if ([cur_xy[0] + 2, cur_xy[1] - 1] != buf[j]):
			loc.append([cur_xy[0] + 2, cur_xy[1] - 1])
			lst.append([cur_xy[0] + 2, cur_xy[1] - 1])
		else:
			loc.append([cur_xy[0] + 2, cur_xy[1] - 1])
			lst.append([cur_xy[0] + 2, cur_xy[1] - 1])
			buf.append(cur_xy)
			return(1)
	if (cur_xy[0] - 2 > 0) and (cur_xy[1] - 1 > 0) and ([cur_xy[0] - 2, cur_xy[1] - 1] not in lst):
		if ([cur_xy[0] - 2, cur_xy[1] - 1] != buf[j]):
			loc.append([cur_xy[0] - 2, cur_xy[1] - 1])
			lst.append([cur_xy[0] - 2, cur_xy[1] - 1])
		else:
			loc.append([cur_xy[0] - 2, cur_xy[1] - 1])
			lst.append([cur_xy[0] - 2, cur_xy[1] - 1])
			buf.append(cur_xy)
			return(1)
	return(0)



j = 0
cout = 1
while a == 0:
	Q.append([])
	for i in len(Q[j])
		a = refresh(Q[j][i])
		if a == 1:
			print(len(Q)-1)
			break;
	cout += 1
	j += 1