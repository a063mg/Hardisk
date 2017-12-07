N = int(input())

def findInt(lst):
	for word in lst:
		pas = 0
		num = 0
		try:
			num = int(word)
		except ValueError:
			pas = 1
		if pas == 0:
			return(num)

def findAmp(lst):
	name = ['боец', 'лекарь']
	for word in lst:
		if word in name:
			return(word)

dic = []

for i in range(N):
	player = input()
	lst = player.split()
	name = lst[0][1:-2]
	damage = findInt(lst)
	amplua = findAmp(lst)
	dic.append({'name': name, 'damage': damage, 'amplua': amplua})