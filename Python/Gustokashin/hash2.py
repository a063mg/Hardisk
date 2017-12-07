lst = [1 for i in range(1000)]
p = 11
for i in range(1,1000):
	lst[i] = lst[i-1]*p

s = input()
h = [0 for i in range(len(s))]
for i in range(len(s)):
	h[i] = (ord(s[i]) - ord('a') + 1)*lst[i]
	if i:
		h[i] += h[i-1]


result = 0
for l in range(1,len(s)+1):
	hs = [ 0 for i in range(len(s)-l+1)]
	for i in range(0,len(s)-l+1):
		curh = h[i+l-1]
		if i:
			curh -= h[i-1]
		curh *= lst[len(s)-i-1]
		hs[i] = curh
	hs.sort()
	result += len(hs)
print(result)
