T = int(input())
for k in range(T):
    N, K = map(int, input().split())
    li2 = []
    wordC = 0
    ind = '1'*K
    for _ in range(N):
        li = input().split()
        li2.append(li)
        li = ''.join(li)
        hor = ''
        for i in li:
            if i == '1':
                hor += i
            else:
                if len(hor) != K:
                    hor = ''
                else:
                    if ind in li:
                        wordC += 1
                        hor = ''
        if (hor == ind) and (ind in li):
            wordC += 1
    tmp2 = ''
    v, h = 0, 0
    for _ in range(N*N):
        tmp2 += li2[v][h]
        v += 1
        if v == N:
            v = 0
            h += 1
            ver = ''
            for j in tmp2:
                if j == '1':
                    ver += j
                else:
                    if len(ver) != K:
                        ver = ''
                    else:
                        if ind in tmp2:
                            wordC += 1
                            ver = ''
            if (ver == ind) and (ind in tmp2):
                wordC += 1
            tmp2 = ''
    print('#%d %d' % (k+1,wordC))