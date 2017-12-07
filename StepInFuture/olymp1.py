a = 1
lst = []
max_sum = 0
mx = 0

while int(a) != 0:
	a = input()
	num = int(a[-1])
	if (num%2 == 0) and num != 0:
		lst.append(int(a))
	else:
		if len(lst) > mx:
			mx = len(lst)
			max_sum = sum(lst)
		lst = []
	# lst.append(a)

print(max_sum)