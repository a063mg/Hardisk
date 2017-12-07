lst = [1 for i in range(1000)]
p = 31
for i in range(1,1000):
	lst[i] = lst[i-1]*p

s = input().split()
s1 = input().split()

for i in range(len(s)):
	Hash = 0
	j = 0
	for k in s[i]:
		Hash += (ord(k) - ord('a') + 1)*lst[j]
		j += 1

for i in range(len(s1)):
	Hash1 = 0
	j = 0
	for k in s1[i]:
		Hash1 += (ord(k) - ord('a') + 1)*lst[j]
		j += 1
g = 0

print(Hash,Hash1)
# h[i] = h[i-1]*10+s[i]
# h[i,k] = h[i+k-1] - h[i-1]*10^k