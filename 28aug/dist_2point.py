import math

def distance(x1, y1, x2, y2):
    p1 = [1, 2]
    p2 = [3, 4]
    distace = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    print(distace)
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist

print(distance(1, 2, 3, 4))




