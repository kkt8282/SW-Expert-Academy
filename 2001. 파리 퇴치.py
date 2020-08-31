a = int(input())
for i in range(a):
    x = 0
    y = 0
    nL = []
    mL = []
    mLsum = 0
    m, n = map(int, input().split())
    for _ in range(m):
        nL.append(list(map(int, input().split())))
    for _ in range((m-n+1)*(m-n+1)):
        if x >= m-n+1:
            x = 0
            y += 1
        for _ in range(n):
            mLsum += sum(nL[y][x:x+n])
            y += 1
        mL.append(mLsum)
        mLsum = 0
        x += 1
        y -= n
    print('#%d %d' % (i+1, max(mL)))