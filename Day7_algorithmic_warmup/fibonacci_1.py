def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(2, n+1):
        c = a + b
        a, b = b, c
    # print(a)
    return c


a = int(input())
print(fibonacci(a))