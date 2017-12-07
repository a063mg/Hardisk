m = int(input())
s = input()
a = []
g = ''

k = 0
j = 0
lst = []
while j < len(s):
	if int(s[j]) == 1:
		lst.append(j)
	k += 1
	j += 1

i = 0
while i < len(lst):
	if i+m >= len(lst):
		a.append((int(lst[len(lst)-1]) - int(lst[i]))*2)
	else:
		a.append((int(lst[i+m]) - int(lst[i]))*2)
	i += 1

j = 0
while j < len(a):
	g += str(a[j])
	g += ' '
	j += 1
print(g)







			

		

