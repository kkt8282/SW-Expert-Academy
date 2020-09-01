T = int(input())
for i in range(T):
    n = int(input())
    sum = 0
    for j in range(1,n+1):
        if j % 2 == 1:
            sum += j
        else:
            sum -= j
    print('#%d %d'%(i+1,sum))