def average_string(s):
    abc = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    cba = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

    num = 0
    text = ''
    s = s.split()
    if s == []:
    	return('n/a')
    for i in s:
    	if i in abc:
    		num  += abc[i]
    	else: 
    		return('n/a')

    num = num/len(s)
    num = int(num)
    for i in range(len(str(num))):
    	text += cba[int(str(num)[i])]
    return(text)