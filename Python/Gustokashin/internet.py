month = list(map(int,input().split()))

s = sum(month)

def one(s):
	trafic = 3000
	price = 350
	if s < trafic:
		return str(price)+' 0'
	else:
		return(str(((s-trafic)//300+(s-trafic)%300)*30+350)+' 0')

def two(month):
	s = sum(month)
	Q = 31
	trafic = 500
	price = 29
	pas = True
	for day in month:
		if day == 0:
			Q -= 1
		if day > trafic:
			pas = False
			return -1
	if pas:
		return str(price*Q)+' 0'

def three(month):
	trafic = 0
	price = 1.2
	for day in month:
		trafic += day
	return str(int(trafic*price))+' '+str(10*int(10*trafic*price-10*int(trafic*price)))

def four(s):
	if s == 0:
		return -1
	else:
		return '790 0'

def five(s):
	trafic = 16000
	price = 590
	if s > trafic:
		return '-1'
	else:
		return str(price)+' 0'

print(one(s))
print(two(month))
print(three(month))
print(four(s))
print(five(s))