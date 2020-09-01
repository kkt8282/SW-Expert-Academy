T = int(input())
for i in range(T):
    n = sorted(list(map(int, input().split())))
    a = round(sum(n[1:len(n)-1])/(len(n)-2))
    print('#%d %d'%(i+1,a))