#code
T = int(input())
for m in range(T):
    i, j = list(map(int, input().split()))
    for k in range(i, j+1):
        str_k = str(k)
        if len(str_k) > 1:
            if len(set(str_k)) != len(str_k):
                continue
        print(k, end=" ")
    print()
        