# Using Hash-maps (optimized solution)

def pairExists(arr, x):
    len_arr = len(arr)

    # Creating an empty set
    set_a = set()
    # Ignoring if length of array is less than 2
    if len_arr < 2:
        return False
    for i in range(len_arr):
        # 0 case must be handled explicitely as 
        # x % 0 is undefined behaviour
        if arr[i] == 0:  # if value of arr[i] is 0
            if x == 0:
                return True
            else:
                return False 

        # x / arr[i] exists in hash then we found a pair
        if x % arr[i] == 0:

            if x // arr[i] in set_a:
                return True 
            set_a.add(arr[i])
    return False

a = [1, 20, 8, 0]
x = 0
if pairExists(a, x):
    print("Yes")
else:
    print("No")

# 1. Create an empty hash table
# 2. Traverse array elements and do following for every element arr[i]
# * if arr[i] is 0 and x is also 0, return true, else ignore arr[i]
# * 

"""def pairExists(arr, n):
    len_arr = len(arr)
    for i in range(len_arr-1):
        for j in range(i+1, len_arr):
            if (arr[i] * arr[j] == n):
                return True 
    return False 

if __name__ == "__main__":
    pair = [0, 20, 9, 50]
    n = 360
    if pairExists(pair, n):
        print("Yes")
    else:
        print("No")
    n = 1000
    if pairExists(pair, n):
        print("Yes")
    else:
        print("No")


# time-Complexity = O(n**2)

"""