# Iterative approach - Time-Complexity = O(k), Space-Complexity = O(1)
# k is the no of digits

def replaceZeros(num):
    num += calculateAddedValue(num)
    return num

def calculateAddedValue(num):
    decimal_place = 1
    result = 0 
    if num == 0:
        result += decimal_place * 5
    
    while num > 0:
        if num % 10 == 0:
            result += (5 * decimal_place)
        num = num // 10
        decimal_place = decimal_place * 10
    return result

a = 102
print(replaceZeros(a))

"""def replaceZero(str):
    a = list(str)
    for i in range(len(a)):
        if a[i] == '0':
            a[i] = '5'
    a ="".join(a)
    return a
"""

