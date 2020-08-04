# Using stack (efficient solution)
def nearestSmallest(arr):
    len_arr = len(arr)
    s = []
    for i in range(len_arr):
        while (len(s) > 0 and s[-1] >= arr[i]):
            s.pop()
        if (len(s) == 0):
            print('_', end = ', ')
        else:
            print(s[-1], end = ', ')
        s.append(arr[i])
        # print('Array: ', s)
    print()        

if __name__ == '__main__':
    a = [1, 3, 0, 2, 5]
    nearestSmallest(a)

# Time complexity - O(n)

"""def nearestSmallest(arr):
    len_arr = len(arr)
    print("_", end = ', ')
    for i in range(1, len_arr):
        for j in range(i-1, -2,-1):
            
            if arr[j] < arr[i]:
                print(arr[j],end = ', ')
                break
            if j == -1:
                print("_",end = ', ')
    print()

if __name__ == "__main__":
    a = [1, 6, 4, 10, 2, 5]
    print(a)
    nearestSmallest(a)

# Time-Complexity - O(n**2)
"""