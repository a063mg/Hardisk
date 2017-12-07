k = str(input())
n = int(input())

s = str(k)
cur = ''
j = 0
buf = ''
for i in range(n-1):
	j = 0
	buf = ''
	while j < len(s):
		x = j
		pas = True
		while s[x] == s[j]:
			if x < len(s)-1:
				x += 1
				pas = False
			else:
				if x == len(s)-1:
					if s[j] == s[x]:
						x+=1
				break
		if pas:
			x+=1
		buf += str(len(s[j:x]))+s[j]
		j = x-1
		j += 1
	s = buf

for i in range(len(s)):
	if i != len(s)-1:
		print(s[i], end=" ")
	else:
		print(s[i])
