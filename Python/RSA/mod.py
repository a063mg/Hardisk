import time
#a = int(input())
#A = int(input())
#B = int(input())
#YA = (B**a)%p
#YB = (B**A)%p
#
#print(YA, YB)
#
#key = (YB**a)%p
#print(key)
# 
#text = int(input())
#decode = text*key%p
def fastExp(b, n):
	global finish
	global start
	start = time.time()
	def even(n):#проверка четности
	    if n%2==0:
	        return 1
	    return 0
	if n==0:
	    return 1
	if even(n):
	    return fastExp(b, n/2)**2
	    finish = time.time()
	    print(finish)
	print(finish)
	finish = time.time()
	return b*fastExp(b, n-1)
fastExp(324823, 328546)
time1 = finish - start
print(time1)

