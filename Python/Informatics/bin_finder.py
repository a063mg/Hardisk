lst = input().split()

N = int(lst[0])
K = int(lst[1])

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

def find1(num, lst):
	L = 0
	R = len(lst)-1
	while (R-L)>1:
		M = round((L+R)/2)
		if num < lst[M]:
			R = M
		else:
			L = M
	# if abs(lst1[R-1]-num) > abs(lst1[R]-num):
	# 	return(lst1[R])
	# else:
	return(lst1[L])

for i in lst2:
	print(find1(i,lst1))

