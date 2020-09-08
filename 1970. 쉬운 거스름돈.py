T = int(input())
for i in range(T):
    mon = int(input())
    mL = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print('#%d'%(i+1))
    for i in mL:
        m = mon // i
        mon -= m*i
        print(m, end=' ')
    print()