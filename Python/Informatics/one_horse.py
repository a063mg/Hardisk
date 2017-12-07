N = int(input())
xy1 = input().split()
xy1[0] = int(xy1[0])
xy1[1] = int(xy1[1]) 
xy2 = input().split()
xy2[0] = int(xy2[0])
xy2[1] = int(xy2[1]) 

loc =[]
lst = [xy1]
Q = [[xy1]]
cur = xy1
ref = 0
a = 0
buf = [xy2]
k = 0
j = 0
step = 0

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


i = 0        
while ref == 0:
	Q.append([])
	loc = []
	for k in range(len(Q[i])):
		cur = Q[i][k]
		ref = refresh(cur)
		if ref == 1:
			a = len(Q)-1
			break;
	Q[i+1] = loc
	i += 1

print(a)

ref = 0
j = 1
while buf[len(buf)-1] != xy1:
	lst = []
	loc = []
	ref = 0
	Q = [[xy1]]
	i = 0  
	while ref == 0:
		Q.append([])
		loc = []
		for k in range(len(Q[i])):
			cur = Q[i][k]
			ref = refresh(cur)
			if ref == 1:
				j += 1
				break;
		Q[i+1] = loc
		i += 1

for j in range(len(buf)):
	print(buf[len(buf)-j-1][0],buf[len(buf)-j-1][1])



