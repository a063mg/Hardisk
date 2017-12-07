n = int(input())

array = list(map(int,input().split()))

ans = array[0]
min_sum = 0
sm = 0

for i in range(n):
	sm += array[i]
	ans = max(ans,sm-min_sum) 
	min_sum = min(sm,min_sum) 
