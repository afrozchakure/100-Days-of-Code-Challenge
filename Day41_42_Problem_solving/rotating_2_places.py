def isRotated(str1, str2):
    if len(str1) != len(str2):
        return False 

    clockwise = ""
    anti_clockwise = ""
    l = len(str2)
    clockwise += str2[l-2:] + str2[:l-2]  
    anti_clockwise += str2[2:] + str2[:2]
    # print(clockwise)
    # print(anti_clockwise)
    return (str1 == clockwise or str1 == anti_clockwise)

if __name__=="__main__":
    str1 = 'jungle'
    str2 = 'azonam'
    if isRotated(str1, str2):
        print("yes")
    else:
        print('NO')