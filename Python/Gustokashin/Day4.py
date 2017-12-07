n = int(input())
m = int(input())
a = int(input())
b = int(input())

N = m-n

if 4*a < b:
	print(N*a)
else:
	if N%4*a < b:
		print((N//4)*b+(N%4)*a)
	else:
		print((N//4)*b+b)