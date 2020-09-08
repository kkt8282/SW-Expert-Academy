T = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for i in range(T):
    N, K = map(int, input().split())
    stuL = []
    idx = 0
    for j in range(1,N+1):
        a = list(map(int, input().split()))
        score = a[0]*0.35 + a[1]*0.45 + a[2]*0.2
        stuL.append([j,score])
    s_stuL= sorted(stuL, key=lambda x: x[1], reverse=True)
    for k in grade:
        for _ in range(int(N/10)):
            s_stuL[idx][1] = k
            if s_stuL[idx][0] == K:
                print('#%d %s'%(i+1, s_stuL[idx][1]))
            idx += 1
