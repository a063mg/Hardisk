N = int(input())

lst = list(map(int, input().split()))
cout = 0
for i in range(N-1):
	pas = True
	pas1 = True
	for j in range(N-1):
		if lst[j] > lst[j+1]:
			cout += 1
			pas = False
			pas1 = False
			buf = lst[j]
			lst[j] = lst[j+1]
			lst[j+1] = buf
	if pas1 and pas:
		break


print(cout)