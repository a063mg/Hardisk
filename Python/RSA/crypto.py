p = int(input())
n = 2
l = 0
i = 1
while n < p:
	print("The number n is ", n)
	i = 1
	while i < p:
		l=(n**i)%p
		if (i==p-1):
			print("Element found: ", n)
		else:
			if(l==1):
				break;
		i += 1
	n += 1
