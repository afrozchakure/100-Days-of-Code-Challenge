import math
def posRightmost(num):
    bin_num = bin(num)[2:]
    len_bin_num = len(bin_num)
    count = 0
    print(bin_num)
    for i in bin_num[::-1]:
        count += 1
        if i == '1':
            return count
    return None

def posRightmost_m2(n):
    return int(math.log2(n&-n) + 1)

num_a = 18
print(posRightmost(num_a))
print(posRightmost_m2(num_a))