N,p,k = list(map(int,input().split()))
lst = list(map(int,input().split()))

lst1 = ''
lst2 = []
cur = p-1

buf = 0
for j in range(N-1):
	a = '-'
	for i in range(N-1):
		if lst[i] > lst[i+1]:
			if i == cur and k > 0:
				k -= 1
				a = '+'
			elif i+1 == cur:
				cur -= 1
			if a != '+':
				if i == cur and k == 0:
					cur += 1
				buf = lst[i+1]
				lst[i+1] = lst[i]
				lst[i] = buf
	# print(lst, cur)
	lst2.append(cur)
	lst1 += str(a)

print(cur+1)
print(lst1)

