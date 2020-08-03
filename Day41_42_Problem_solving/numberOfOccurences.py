#code
T = int(input())
for i in range(T):
    # X - element whose occurence needs to be counted
    N, X = list(map(int, input().split()))  
    list_X = list(map(int, input().split()))
    count = 0
    for i in list_X:
        if i == X:
            count += 1
    if count > 0:
        print(count)
    else:
        print("-1")
    