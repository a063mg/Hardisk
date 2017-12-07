M = int(input())

for i in range(M//4):
    if (M-i*4)%3 == 0: 
        print(i)
        print((M-i*4)//3)
        break;