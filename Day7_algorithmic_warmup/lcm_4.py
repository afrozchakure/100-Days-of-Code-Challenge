def gcd(a, b):
    if b == 0:
        return a
    a1 = a % b 
    return gcd(b, a1)

def lcm(a, b):
    return int(a*b / gcd(a, b))

x, y = list(map(int, input().split()))
if y > x:
    x, y = y, x
print(lcm(x, y))
