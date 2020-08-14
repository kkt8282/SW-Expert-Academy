a = int(input())
for i in range(a):
    b = int(input())
    days = list(map(int, (input().split())))
    result = 0
    price = days[-1]
    for day in days[-2::-1]:
        if day < price:
            result += (price-day)
        else: 
            price = day
    print('#%d %d' % (i+1, result))