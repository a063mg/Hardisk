n = int(input())

a = ''
k = str(n)

if int(k[len(k)-1]) == 0:
	a = 'ek'
elif int(k[len(k)-1]) == 1:
	a = 'ka'
elif int(k[len(k)-1]) == 2 or int(k[len(k)-1]) == 3:
	a = 'ki'
else:
	a = 'ek'
if n < 10:
	if int(k[len(k)-1]) == 0:
		a = 'ek'
	if int(k[len(k)-1]) == 1:
		a = 'ka'
	if int(k[len(k)-1]) > 2 and n < 5: 
		a = 'ki'
if n > 10 and n < 19:
	a = 'ek'
print(n, 'boch'+a)
