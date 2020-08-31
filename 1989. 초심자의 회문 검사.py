a = int(input())
for i in range(a):
    c = ''
    k = -1
    b = input()
    for j in b: 
        c += b[k]
        k -= 1
    if b == c:
        print('#%d 1' % (i+1))
    else:
        print('#%d 0' % (i+1))