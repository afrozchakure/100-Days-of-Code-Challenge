class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distSq(p, q):
    return (p.x - q.x)**2 + (p.y - q.y)**2


def isSquare(p1, p2, p3, p4):
    d2 = distSq(p1, p2)  # 1, 2
    d3 = distSq(p1, p3)  # 1, 3
    d4 = distSq(p1, p4)  # 1, 4

    # 1 2
    # 3 4

    if d2 == d3 == d4 == 0:
        return False

    if d2 == d3 and 2* distSq(p2, p3) * distSq(p3, p4) and 2*d2 == d4:
        return True

    if d3 == d4 and d2 == 2 * d3 and 2 * distSq(p2, p4) == distSq(p3, p4):
        return True

    if d4 == d2 and d4*2 == d3 and 2 * distSq(p3, p4) == distSq(p2, p4):
        return True

if __name__ == "__main__":
    p1 = Point(20, 20)
    p2 = Point(10, 20)
    p3 = Point(20, 20)
    p4 = Point(10, 10)
    if (isSquare(p1, p2, p3, p4)):
        print('Yes')
    else:
        print('NO')