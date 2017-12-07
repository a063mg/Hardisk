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
	while i <= n:
		j = 0
		while j <=  n/7+1:
			f = 0
			while f <= n/28+1:
				if i + 7*j + 28*f >= n: 
					if Bool == True: 
						minim = (i*a + j*b + f*c)
						Bool = False
					if (i*a + j*b + f*c) < minim:
						minim = (i*a + j*b + f*c)
				f += 1
			j += 1
		i += 1
	return(minim)

print(goto())
