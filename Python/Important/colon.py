n = int(input())
pillar = input().split()

for i in range(len(pillar)):
	pillar[i] = int(pillar[i])

aver = []
buf = 0
differ = []
pas = 0

for i in range(n-1):
	differ.append(abs(pillar[i] - pillar[i+1]))
aver = sum(buf)//(n-1)


for i in range(len(pillar)):
	if differ[i] != aver:
		if differ[i] > aver:
			if differ[i+1] > aver:
				while buf != aver: 
					buf = abs(pillar[i] - pillar[i+1])
					pillar[i] += 1
			else:




		


























	# a = 0
	# for i in range(n-1):
	# 	const = abs(pillar[i] - pillar[i+1])
	# 	if abs(pillar[i] - pillar[i+1]) != const:
	# 		a = 1
	# if a == 0:
	# 	pas = 1
	# 	break;