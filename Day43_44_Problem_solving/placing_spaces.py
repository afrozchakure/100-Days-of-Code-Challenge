"""def printInterleaved(str, idx):
    if idx >= len(str):
        print(str)
        return
    printInterleaved(str[:idx] + " " + str[idx:], idx + 2)
    printInterleaved(str, idx + 1)
    return
printInterleaved('ABCDE', 1)
"""
#code
def perm_space(str):
    n = len(str)
    opsize = int(pow(2, n-1))
    ans = []
    for counter in range(opsize):
        str_ans = ""
        str_ans += "("
        for j in range(n):
            str_ans += str[j]
            if (counter & (1 << j)):
                # print("\ncounter: %d j: %d, 1<<j: %d, counter & 1<<j: %d" %(counter, j, 1<<j, counter & 1<<j))
                str_ans += " "
        str_ans += ")"
        ans.append(str_ans)
    ans.sort()
    # print(ans)
    print("".join(ans))
        # print("\n", end="")
        
n = int(input())
for i in range(n):
    str1 = input()
    perm_space(str1)