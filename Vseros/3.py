genom1 = input()
genom2 = input()

count = 0

for i in range(len(genom1)-1):
	if genom2.find(genom1[i:i+2]) != -1:
		count += 1
print(count)
