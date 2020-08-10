#code
def pairExist(sum_pairs, A):
    for i in range(len(A)):
        diff = sum_pairs - A[i]
        if (int(diff) > 0 and diff in A[i+1:]):
            # print(A[i], diff)
            return "Yes"
    return "No"
T = int(input())
for i in range(T):
    N, sum_pairs = list(map(int, input().split()))
    A = list(map(int, input().split()))
    answer = pairExist(sum_pairs, A)
    print(answer)
