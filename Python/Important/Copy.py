tar = input().split()
a = int(tar[0])
b = int(tar[1])
c = int(tar[2])
n = int(input())

# if c/28 > b/7:
#  if a > b/7:
#  	n*a
#  else:
#  	(n-n%7)/7*b
#  	if a/(n-n%7) > b/7/(n-n%7):
#  		print((n-n%7)/7*b + a*n)
#  	else:
#  		print((n-n%7)/7*b + b)
# else: 

i = 0
j = 0
f = 0

def goto():
	Bool = True
	i = 0
	j = 0
	f = 0
	if a <= b/7 and a <= c/28:
		return(a*n)
	if a >= b/7 and b/7 >= c/28:
		p1 = n//28
		r1 = n%28
		p2 = r1//7
		r2 = r1%7
		s1 = p1*c + p2*b + a*r2
		s2 = p1*c + (p2+1)*b
		s3 = (p1 + 1)*c
		if s1 < s2 and s1 < s3:
			return(s1)
		else:
			if s2 <= s3 and s2 <= s1:
				return(s2)
			else:
				return(s3)  
	if b <= a*7 and c >= b*4 and a*28 >= c:
		if (n//7)*b + a*(n%7) >= (n//7+1)*b:
			return((n//7+1)*b)
		else:
			return(n//7)*b + a*(n%7)
	if b <= a*7 and c >= b*4 and a*28 <= c:
		if (n//7)*b + a*(n%7) >= (n//7+1)*b:
			return((n//7+1)*b)
		else:
			return(n//7)*b + a*(n%7) 

	if c <= a*28 and a*7 <= b and b*4 >= c:
		if (n//28)*c + a*(n%28) >= (n//28+1)*c:
			return((n//28+1)*c)
		else:
			return(n//28)*c + a*(n%28) 	
	return("")

print(goto())
