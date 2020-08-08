#code
T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort() # n 
    diff = 10**20 # initialize difference as infinite
    for i in range(len(arr)-1):  # nlogn
        if((arr[i+1] - arr[i]) < diff):
            diff = arr[i+1] - arr[i]
    print(diff) 
            
# Time Complexity - O(nlogn)