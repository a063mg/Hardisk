N = int(input())


workers = list(map(int, input().split()))
taxi = list(map(int, input().split()))
lst = list(range(N))
lst1 = list(range(N))

for i in range(N-1):
	pas1 = True
	pas2 = True
	for j in range(N-1):
		if workers[j] > workers[j+1]:
			pas2 = False
			buf = lst[j]
			lst[j] = lst[j+1]
			lst[j+1] = buf
			buf = workers[j+1]
			workers[j+1] = workers[j]
			workers[j] = buf
		if taxi[j] < taxi[j+1]:
			pas1 = False
			buf = lst1[j]
			lst1[j] = lst1[j+1]
			lst1[j+1] = buf
			buf = taxi[j+1]
			taxi[j+1] = taxi[j]
			taxi[j] = buf
	if pas1 and pas2:
			break

# for i in range(N):
# 	for j in range(N-1):
# 		if lst[j] > lst[j+1]:
# 			buf = lst1[j]
# 			lst1[j] = lst1[j+1]
# 			lst1[j+1] = buf
# 			buf = lst[j+1]
# 			lst[j+1] = lst[j]
# 			lst[j] = buf

list1 = [0 for i in range(N)]

for i in range(len(lst)):
	list1[lst[i]] = i
	
for i in list1:
	print(lst1[i]+1,end = " ")


