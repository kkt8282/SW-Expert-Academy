a=int(input())
for i in range(a):
    b = int(input())
    fL = []
    print("#%d" % (i+1))
    for j in range(b):
        sL = [1, 1]
        g = 1
        if j == 0:
            fL.append(1)
            print(*fL)
        elif j == 1:
            fL.append(1)
            print(*fL)
        elif j == 2:
            fL.insert(1, 2)
            print(*fL)
        else: 
            for _ in range(j-1):
                h = fL[g-1] + fL[g] 
                sL.insert(g, h)
                g += 1
            fL = sL
            print(*sL)