n = int(input())

prime = []

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in list(range(3, int(num**0.5)+2, 2)):
        if num % n == 0:
            return False
    return True

for i in range(2, n+1):
	if n%i == 0 and is_prime(i):
		prime.append(i)


prime.sort()

pr = ''

for i in prime:
	pr += str(i)
	pr += ' '

print(pr)