lst = input().split()
a = int(lst[0])
b = int(lst[1])
c = int(lst[2])
num = int(lst[3])

lst = []
for j in range(num//a):
	a1 = j*a
	for k in range(((num-a1)//b)+1):
		b1 = k*b
		c1 = num-b1-a1
		if c1 >= 0:
			if c1%c == 0:
				lst.append([j,k,c1//c])

print(len(lst))
for i in lst:
	print(i[0],i[1],i[2])