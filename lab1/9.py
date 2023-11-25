import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def circle_relationship(x1, y1, r1, x2, y2, r2):
    dist = distance(x1, y1, x2, y2)

    if dist + r1 < r2:
        return "C1 is in C2"
    elif dist + r2 < r1:
        return "C2 is in C1"
    elif dist <= r1 + r2:
        return "Circumference of C1 and C2 intersect"
    else:
        return "C1 and C2 do not overlap"

x1, y1, r1, x2, y2, r2 = map(float, input().split())

print(circle_relationship(x1, y1, r1, x2, y2, r2))
