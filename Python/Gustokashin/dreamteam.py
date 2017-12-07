N = int(input())

team = []

for i in range(N):
	team.append(int(input()))

team.sort()

mx = team[0]+team[1]

s = 0
for i in team:
	for i in team:
		if i <= mx:
			s += i