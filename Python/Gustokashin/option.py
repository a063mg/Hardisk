string = str(input())

answer = string
j = 1

dic = {}
def replase(string,i,j):
	return string[0:i]+str(j)+string[i+1:len(string)]

# pas = True
# while pas:
# 	L = -1
# 	R = -1

pas = True
k= 0
while pas:
	L = 0
	R = 0
	for i in range(len(string)):
		if string[i] == '(':
			L = i
		if string[i] == ')':
			R = i
			break
	if L == R == 0:
		pas = False
		break
	for i in range(L,R):
		if string[i] == "*":
			string = replase(string,i,'0')
			if dic.get(i,'no') == 'no':
				dic[i] = j
				j += 1
	for i in range(L,R):
		if string[i] == "+":
			string = replase(string,i,'0')
			if dic.get(i,'no') == 'no':
				dic[i] = j
				j += 1
	string = replase(string,L,'&')
	string = replase(string,R,'@')

for i in range(len(answer)):
	if answer[i] == "*":
		if dic.get(i,'no') == 'no':
			dic[i] = j
			j += 1
for i in range(len(answer)):
	if answer[i] == "+":
		if dic.get(i,'no') == 'no':
			dic[i] = j
			j += 1

for i in range(len(answer)):
	if dic.get(i,'no') == 'no':
		print(answer[i],end="")
	else:
		print(dic[i],end="")

