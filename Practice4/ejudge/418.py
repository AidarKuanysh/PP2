x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

y2r = -y2

t = y1 / (y1 - y2r)
x = x1 + t * (x2 - x1)

print(f"{x:.10f} 0.0000000000")