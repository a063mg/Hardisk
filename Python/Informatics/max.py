import math
a = int(input())
b = int(input())
c = a - b
if c == 0:
	print(a)
else:
	if math.fabs(c)/c == -1.0:
		print(b)
	else:
		print(a) 