A = int(input())
B = int(input())
C = int(input())

n = 0
f = 0
if A%2 == 0 or B%2 == 0 or C%2 == 0:
	n = 1
if A%2 != 0 or B%2 != 0 or C%2 != 0:
	f = 1
if f == 1 and n == 1:
	print('YES')
else:
	print('NO')

