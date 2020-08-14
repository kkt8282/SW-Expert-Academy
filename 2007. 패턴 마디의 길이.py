a = int(input())
for i in range(a):
    b = input()
    k = ''
    idx=1
    idx2=2
    for j in b:
        k += j
        if k != b[idx:idx2]:
            idx += 1
            idx2 += 2
        else:
            break
    print('#%d %d'%(i+1, len(k)))