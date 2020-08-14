a = int(input())
for i in range(1, a+1):
    i = str(i)
    b = i.count('3') + i.count('6') + i.count('9')
    if (b) == 0:
        print(i, end=' ')
    else:
        print('-'*b, end=' ')