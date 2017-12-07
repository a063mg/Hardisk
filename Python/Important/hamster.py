def sort(string):
	a = 0
	b = 0
	lst = [i for i in string]
	buf = ''
	while a == 0: 
		b = 0
		for i in range(len(lst)-1):
			if lst[i] > lst[i+1]:
				buf = lst[i]
				lst[i] = lst[i+1]
				lst[i+1] = buf
				b = 1
		if b == 0:
			a = 1
			break;

	text = ''
	for i in lst:
		text += i
	return(text) 

def clear(string):
	text = ''
	for i in string:
		if i not in text:
			text += i
	return(text)


def hamster_me(code, message):
	index = []
	key = []
	ans = ''
	lst = []
	code = clear(code)
	code = sort(code)
	for i in range(len(code)):
		lst.append([code[i]])

	for i in range(len(lst)-1):
		cur = chr(ord(lst[i][len(lst[i])-1])+1)
		while cur != lst[i+1][0]:
			cur = chr(ord(lst[i][len(lst[i])-1])+1)
			if cur != lst[i+1][0]:
				lst[i].append(cur)

	cur = chr(ord(lst[i][len(lst[i])-1])+1)
	while cur != 'z':
		cur = chr(ord(lst[-1][len(lst[-1])-1])+1)
		lst[-1].append(cur)

	cur = 'a'
	buf = 96
	while cur != lst[0][0]:
		buf += 1
		cur = chr(buf)
		if cur != lst[0][0]:
			lst[-1].append(cur)

	for i in range(len(message)):
		for j in range(len(lst)):
			for k in range(len(lst[j])):
				if message[i] == lst[j][k]:
					key.append(k+1)
					index.append(code[j])

	i = 0
	j = 0
	while i < len(index):
		ans += index[i]
		ans += str(key[j])
		i += 1
		j += 1

	return(ans)












