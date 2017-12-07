lst = [1 for i in range(1000)]
p = 31
for i in range(1,1000):
	lst[i] = lst[i-1]*p

s = input()
i1 = int(input())
i2 = int(input())
ln = int(input())

h = [0 for i in range(len(s))]

for i in range(len(s)):
	h[i] = (ord(s[i]) - ord('a') + 1)*lst[i]
	if i:
		h[i] += h[i-1]

h1 = h[i1-1+ln]
if i1 != 0:
	h1 -= h[i1-1]
h2 = h[i2-1+ln]
if i2 != 0:
	h2 -= h[i2-1]

p1 = lst[i2-i1]*h1

print(h2,p1)



