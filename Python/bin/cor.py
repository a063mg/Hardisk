x = int(input())
y = int(input())

if x**2 + y**2 <= 4: 
	if y <= x and y >= 0 and x >= 0:
		print('YES')
	elif y >= 0 and x <= 0:
		print('YES')
elif y >= -2 and y <= x and x <= 0:
	print('YES')
else:
	print('NO')