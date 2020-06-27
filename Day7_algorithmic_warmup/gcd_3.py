def GCD(a, b):
    if b == 0:
        return a 
    a1 = a % b 
    return GCD(b, a1)

a, b = list(map(int, input().split()))
if b > a:
    a, b = b, a  
print(GCD(a, b))