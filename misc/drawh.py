import math


def drawHTree(center, length, depth):
    """
    1,  4,   16,  64
    2^0 2^2, 2^4, 2^6,
    1   2    3    4

    O(2^(2n-2)) draws
    """
    if depth == 0:
        return []

    next_centers = drawH(center, length)
    for nc in next_centers:
        drawHTree(nc, length * math.sqrt(2), depth - 1)


def drawLine(a, b):
    print(f"p1: {a}, p2: {b}")


def drawH(center, w):
    x, y = center
    left = (x - w / 2, y)
    right = (x + w / 2, y)

    tl = (x - w / 2, y + w / 2)
    bl = (x - w / 2, y - w / 2)

    tr = (x + w / 2, y + w / 2)
    br = (x + w / 2, y - w / 2)

    drawLine(left, right)
    drawLine(tl, bl)
    drawLine(tr, br)

    return tl, bl, tr, br


drawHTree((0, 0), 1, 3)
