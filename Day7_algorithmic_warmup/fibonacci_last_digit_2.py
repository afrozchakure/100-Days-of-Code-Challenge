def fibonacci_last_digit(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(2, n+1):
        c = (a + b) % 10
        a, b = b, c
    # print(a)
    return c

n = int(input())
print(fibonacci_last_digit(n))