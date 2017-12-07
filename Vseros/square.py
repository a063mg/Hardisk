lst = input().split()
A = int(lst[0])
B = int(lst[1])

count = 0

def refresh(A, B):
	global count
	if A == B:
		print(count+1)
		return count
	if A > B:
		A -= round(((A-B)//B))*B
		count += round(((A-B)//B))
		refresh(A,B)
	else:
		B -= round(((B-A)//A))*A
		count += round(((B-A)//A))
		refresh(A,B)

refresh(A,B)