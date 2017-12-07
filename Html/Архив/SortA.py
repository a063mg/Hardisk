def alan(arr):
    lst = ['Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway']
    lst_bool = [0, 0, 0, 0]
    for i in arr:
    	for j in lst:
    		if arr[i] == lst[j]:
    			lst_bool[j] = 1

    a = 0
    for i in lst_bool:
    	if lst_bool[i] == 0:
    		a = 1

    if a == 1:
    	print('No, seriously, run. You will miss it.')
    else:
    	print('Smell my cheese you mother!'
