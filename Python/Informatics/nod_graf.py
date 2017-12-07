A = input().split()
A[0] = int(A[0])
A[1] = int(A[1])

lst = []
a = 0
C = []
for i in range(A[1]):
	C.append(0)

for i in range(A[0]):
	B = input().split()
	for j in range(A[1]):
		B[j] = int(B[j])
	B.append(0)
	lst.append(B)	
lst.append(C)

dont = [[0,0]]
loc = [[[0, 0]]]
strint = 0

def refresh(curxy):
	char = [curxy[0], curxy[1]]
	while (lst[char[1]][char[0]+1] != 1) and (char[0]+1 < A[1]):
		char = [char[0] + 1, char[1]]

		if lst[char[1]][char[0]] == 2:
			dont.append(char)
			loc[count].append(char)
			return(1)
		
	if (char[0] < A[1]) and (char not in dont):
		if lst[char[1]][char[0]] != 2:
			dont.append(char)
			loc[count].append(char)
		else:
			dont.append(char)
			loc[count].append(char)
			return(1)

	char = [curxy[0], curxy[1]]
	while (lst[char[1]][char[0]-1] != 1) and (char[0]-1 >= 0):
		char = [char[0] - 1, char[1]]

		if lst[char[1]][char[0]] == 2:
			dont.append(char)
			loc[count].append(char)
			return(1)
	if (char[0] >= 0) and (char not in dont) and (lst[char[1]][char[0]] != 1):
		if lst[char[1]][char[0]] != 2:
			dont.append(char)
			loc[count].append(char)
		else:
			dont.append(char)
			loc[count].append(char)
			return(1)

	char = [curxy[0], curxy[1]]
	while (lst[char[1]+1][char[0]] != 1) and (char[1]+1 < A[0]):
		char = [char[0], char[1]+1]

		if lst[char[1]][char[0]] == 2:
			dont.append(char)
			loc[count].append(char)
			return(1)
		
	if (char[1] < A[0]) and (char not in dont) and (lst[char[1]][char[0]] != 1):
		if lst[char[1]][char[0]] != 2:
			dont.append(char)
			loc[count].append(char)
		else:
			loc[count].append(char)
			dont.append(char)
			return(1)

	char = [curxy[0], curxy[1]]
	while (lst[char[1]-1][char[0]] != 1) and (char[1]-1 >= 0):
		char = [char[0], char[1]-1]

		if lst[char[1]][char[0]] == 2:
			dont.append(char)
			loc[count].append(char)
			return(1)
		
	if (char[1] >= 0) and (char not in dont) and (lst[char[1]][char[0]] != 1):
		if lst[char[1]][char[0]] != 2:
			dont.append(char)
			loc[count].append(char)
		else:
			loc[count].append(char)
			dont.append(char)
			return(1)

	return(0)

count = 1
j = 0
while a == 0:
	loc.append([])
	for i in range(len(loc[j])):
		a = refresh(loc[j][i])
		if a == 1:
			print(len(loc)-1)
			strint = len(loc)-1
			break;
	count += 1
	j += 1

