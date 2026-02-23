import math

r = float(input().strip())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

a = dx*dx + dy*dy
b = 2 * (x1*dx + y1*dy)
c = x1*x1 + y1*y1 - r*r

if a == 0:
    if x1*x1 + y1*y1 <= r*r:
        print("0.0000000000")
    else:
        print("0.0000000000")
    exit()

disc = b*b - 4*a*c

if disc < 0:
    print("0.0000000000")
    exit()

sqrt_disc = math.sqrt(disc)
t1 = (-b - sqrt_disc) / (2*a)
t2 = (-b + sqrt_disc) / (2*a)

lo = max(0.0, min(t1, t2))
hi = min(1.0, max(t1, t2))

if hi <= lo:
    print("0.0000000000")
else:
    length = math.hypot(dx, dy) * (hi - lo)
    print(f"{length:.10f}")