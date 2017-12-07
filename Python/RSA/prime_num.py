import time
#adding some color
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prRed(prt): print("\033[1;31m {}\033[1;m".format(prt))
def prBlue(prt): print("\033[1;34m {}\033[1;m" .format(prt))
time1 = 0

#waiting for input from user
print(' Hi!')
prGreen("I can calculate all the primes from 0 to n insanely fast")
prBlue("For your own sake, don't use n > 10.000.000 unless you want to wait for a few minutes")

while True:
	try:
		n = int(input(" Enter n = "))
	except ValueError:
		prRed("Sorry, i cant read this number, please try again...")
	else:
		break

#go!
start = time.time()

#calculation
a = list(range(n+1))
a[1] = 0
lst = []
buf = 0
mx = 0
buf1 = []

i = 2
while i <= n:
	if a[i] != 0:
		if a[i] - buf > mx:
			mx = a[i] - buf
		if a[i] - buf > 170:
			buf1.append([a[i], buf])
		buf = a[i]
		lst.append(a[i])
	for j in list(range(i, n+1, i)):
		a[j] = 0
	i += 1

del(lst[0])
#calculation done! It's time to update time
finish = time.time()
time1 = finish - start

#printing list of all prime numbers in range
prBlue(lst)
prRed(buf1)
prRed(mx)

#and some fun facts
print("I found ", len(lst), " prime numbers for ", time1, " seconds...")