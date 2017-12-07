n = int(input())

array = list(map(int,input().split()))

lst = []
sm = 0

for i in array:
	sm += i
	lst.append(sm)

counter = {}	
mx = array[0]
rx = 1
lx = 1
l = 1
ls = []
r = 1
num = 0

j = 0
for i in range(n):
	sm += array[i]
	lst.append(sm)
	if counter.get(array[i],'empty') == 'empty':
		counter[array[i]] = [i]
		num = array[i]
		if num > mx:
			mx = num
			rx = i+1
			lx = i+1
	else:
		for j in range(len(counter[array[i]])):
			if counter[array[i]][j] != 0:
				num = lst[i]-lst[counter[array[i]][j]-1]
				if num > mx:
					mx = num
					rx = i+1
					lx = counter[array[i]][j]+1
			else:
				num = lst[i]
				if num > mx:
					mx = num
					rx = i+1
					lx = 1
		ls = counter[array[i]]
		ls.append(i) 
		counter[array[i]] = ls


print(mx)
print(lx,rx)