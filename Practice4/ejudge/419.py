import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

def dist(xa, ya, xb, yb):
    return math.hypot(xa - xb, ya - yb)

d = dist(x1, y1, x2, y2)

d1 = math.hypot(x1, y1)
d2 = math.hypot(x2, y2)


if d1 <= r or d2 <= r:
    print(f"{d:.10f}")
    exit()


cross = abs(x1 * y2 - y1 * x2)
h = cross / d

dot1 = x1 * (x2 - x1) + y1 * (y2 - y1)
dot2 = x2 * (x1 - x2) + y2 * (y1 - y2)

if h >= r or dot1 < 0 or dot2 < 0:
    print(f"{d:.10f}")
    exit()


t1 = math.sqrt(d1 * d1 - r * r)
t2 = math.sqrt(d2 * d2 - r * r)


ang1 = math.atan2(y1, x1)
ang2 = math.atan2(y2, x2)
delta = abs(ang2 - ang1)
delta = min(delta, 2 * math.pi - delta)


a1 = math.acos(r / d1)
a2 = math.acos(r / d2)

arc = r * (delta - a1 - a2)

print(f"{t1 + t2 + arc:.10f}")