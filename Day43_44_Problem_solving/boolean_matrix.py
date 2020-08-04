# Space optimized solution
def modifyMatrix(mat):

    # Variables to check 
    # if there is 1 in 1st row and col
    row_flag = False
    col_flag = False 

    # Updating the first row and column
    # if 1 is encountered
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            if (i == 0 and mat[i][j] == 1):
                row_flag = True 
            if (j == 0 and mat[i][j] == 1):
                col_flag = True 

            if(mat[i][j] == 1):
                mat[0][j] = 1
                mat[i][0] = 1
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            if(mat[0][j] == 1 or mat[i][j] == 1):
                mat[i][j] = 1
    
    # modify first row if there was any 1
    if (row_flag == True):
        for i in range(len(mat)):
            mat[0][j] = 1

    # modify first column if there was any 1
    if (col_flag == True):
        for i in range(len(mat)):
            mat[i][0] = 1

# A utility function to print a 2D matrix 
def printMatrix(mat) : 
      
    for i in range(0, len(mat)) : 
        for j in range(0, len(mat) + 1) : 
            print( mat[i][j], end = "" ) 
          
        print() 
          
# Driver Code 
mat = [ [1, 0, 0, 1], 
        [0, 0, 1, 0], 
        [0, 0, 0, 0] ] 
          
print("Input Matrix :") 
printMatrix(mat) 
      
modifyMatrix(mat) 
      
print("Matrix After Modification :") 
printMatrix(mat) 

# Time Complexity - O(M*N) and Auxillary Space - O(1)
"""# Using two temporary arrays

#code
T = int(input())
for k in range(T):
    r, c = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for i in range(r)]
    
    # Make two temporary arrays
    row = [0] * r
    col = [0] * c
    
    # Initialize Rows and Columns
    for i in range(r):
        row[i] = 0
    for j in range(c):
        col[j] = 0
        
    # Setting rows and cols to be marked as 1
    # in row[] and col[] arrays
    for i in range(r):
        for j in range(c):
            if (mat[i][j] == 1):
                row[i] = 1
                col[j] = 1
    # Modifying the original array
    for i in range(r):
        for j in range(c):
            if (row[i] == 1 or col[j] == 1):
                mat[i][j] = 1
    
    # print the array
    
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end=" ")
        print()
        
# Time Complexity - O(M*N) and Space Complexity - O(M+N)"""