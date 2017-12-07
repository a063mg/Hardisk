A = int(input())
B = int(input())
C = int(input())

if A >= B and A >= C:
	if B >= C:
		print(C,B,A)
	else:
		print(B,C,A)
elif B >= A and B >= C:
	if A >= C:
		print(C,A,B)
	else:
		print(A,C,B)
elif C >= A and C >= B:
	if A >= B:
		print(B,A,C)
	else:
		print(A,B,C)