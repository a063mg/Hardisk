def replase(string, i, char):
	return(string[0:i]+char+string[i+1:len(string)])

dic = {}

for num in range(97,127):
	dic[chr(num)] = num

pas = True

while pas:
	option = str(input('Do you want to add check symbols? (Y/N)?\n'))

	allowed = ['y', 'n']

	if option.lower() not in allowed:
		print('I dont understand u...')
	else:
		pas = False


pas = True

while pas:
	string = str(input('Enter your word: \n'))
	for char in string:
		if dic.get(char,'nothing') == 'nothing':
			pas = False
	if pas == True:
		pas = False
	else:
		print('Not correct form...')
		pas = True
if option.lower() == 'y':
	sm1 = 0
	sm2 = 0
	i = 3
	for char in string:
		sm1 += ord(char)-96
		sm2 += (ord(char)-96)*i
		i += 1

	a = (29-sm1%29)
	b = (29-sm2%29)

	num2 = (b-a)%29
	num1 = (a - num2)%29

	print(chr(num1+96)+chr(num2+96)+string)
else:
	sm1 = 0
	sm2 = 0
	i = 1
	for char in string:
		sm1 += ord(char)-96
		sm2 += (ord(char)-96)*i
		i += 1

	a = (sm1%29)
	b = (sm2%29)

	i = 0

	while (a*i)%29 != b:   
		i+=1



	num = (ord(string[i-1])-96-a)%29

	char = chr(num+96)

	string = replase(string,i-1,char)

	print(string[2:len(string)])


