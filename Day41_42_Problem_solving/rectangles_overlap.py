class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

def recOverlap(l1, r1, l2, r2):
    # if rectangle is to the left side of one another
    if (l1.x >= r2.x) or (l2.x >= r1.x):
        print('hi')
        return False
    # if rectangle is one above the other
    if (l1.y <= r2.y) or (l2.y <= r1.y):
        print('yo')
        return False
    return True

if __name__ == "__main__":
    l1 = Point(0, 10)  
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)
    if recOverlap(l1, r1, l2, r2):
        print("Overlap")
    else:
        print('Do not overlap')