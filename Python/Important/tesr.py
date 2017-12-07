import random
x = 2 * 10**4
y = 2 * 10**5
f = open('test.txt', 'w')
f.write('%d %d\n1 1' % (x, y))

for i in range(x):
	f.write('0 ')

f.write('\n')

for i in range(y):
	f.write('%d %d\n' % (random.randint(1, x), random.randint(1, x)))

f.close()
