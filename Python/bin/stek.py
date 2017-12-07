commands = []
 
in_put = 0
 
while in_put != '':
    try:
        in_put = input()
        if in_put != '':
            commands.append(in_put)
    except EOFError:
        in_put = ''
 
stek = []
 
error = False
 
for comand in commands:
    if error:
        break;
    znak = comand[0]
    if znak == '+':
        num = comand[1:len(comand)]
        stek.append(num)
    else:
        if len(stek) != 0:
            del stek[-1]
        else:
            error = True
            print('ERROR')
 
if not error:
    if len(stek) != 0:
        buf = ''
        for i in stek:
            buf += i
            buf += ' '
        print(buf[0:len(buf)-1])
    else:
        print('EMPTY')
