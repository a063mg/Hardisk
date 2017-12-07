n,k = map(int,input().split())

obj = []


for i in range(n):
	obj.append([])
	a,b = map(int,input().split())
	obj[i].append(a)
	obj[i].append(b)

dic = {}



for i in obj:
	dic[i[1]] = dic.get(i[1],[])
	dic[i[1]].append(i[0])
	num = dic.get(i[1])
	num.sort()
	dic[i[1]] = num

keys = list(dic.keys())

step = (dic[keys[0]][0] - 1)+(keys[0]-1)
maystep = 0
cur = dic[keys[0]][0]
for j in range(len(keys)):
	if keys[j] != keys[-1]:
		step += abs(keys[j+1]-keys[j])
	if (dic[keys[j]][0] < cur < dic[keys[j]][-1]):
		if abs(dic[keys[j]][-1]-cur) > abs(dic[keys[j]][0]-cur):
			if abs(dic[keys[j+1]][-1] - dic[keys[j]][-1]) < abs(dic[keys[j+1]][-1] - dic[keys[j]][0]):
				step += 2*abs(dic[keys[j]][0]-cur)+abs(dic[keys[j]][-1]-cur)
				cur = dic[keys[j]][-1]
			else:
				step += 2*abs(dic[keys[j]][-1]-cur)+abs(dic[keys[j]][0]-cur)
				cur = dic[keys[j]][0]
		else:
			if abs(dic[keys[j+1]][0] - dic[keys[j]][-1]) > abs(dic[keys[j+1]][0] - dic[keys[j]][0]):
				step += 2*abs(dic[keys[j]][-1]-cur)+abs(dic[keys[j]][0]-cur)
				cur = dic[keys[j]][0]
			else:
				step += 2*abs(dic[keys[j]][0]-cur)+abs(dic[keys[j]][-1]-cur)
				cur = dic[keys[j]][-1]
	else:
		if abs(dic[keys[j]][-1]-cur) > abs(dic[keys[j]][0]-cur):
			step += abs(dic[keys[j]][0]-cur)
			step += abs(dic[keys[j]][0]-dic[keys[j]][-1])
			cur = dic[keys[j]][-1]
		else:
			step += abs(dic[keys[j]][-1]-cur)
			step += abs(dic[keys[j]][-1]-dic[keys[j]][0])
			cur = dic[keys[j]][0]
print(step)


