import math

r = float(input().strip())
ax, ay = map(float, input().strip().split())
bx, by = map(float, input().strip().split())

def line_intersects_circle(ax, ay, bx, by, r):
    dx = bx - ax
    dy = by - ay
    
    if dx == 0 and dy == 0:
        return math.sqrt(ax*ax + ay*ay) > r
    
    t = -(ax*dx + ay*dy) / (dx*dx + dy*dy)
    
    if t < 0:
        t = 0
    elif t > 1:
        t = 1
    
    cx = ax + t * dx
    cy = ay + t * dy
    
    dist_to_origin = math.sqrt(cx*cx + cy*cy)
    
    return dist_to_origin < r

def find_tangent_points(px, py, r):
    d = math.sqrt(px*px + py*py)
    
    if d == r:
        return [(px, py)]
    
    l = math.sqrt(d*d - r*r)
    
    theta = math.acos(r / d)
    
    phi = math.atan2(py, px)
    
    angle1 = phi + theta
    angle2 = phi - theta
    
    x1 = r * math.cos(angle1)
    y1 = r * math.sin(angle1)
    
    x2 = r * math.cos(angle2)
    y2 = r * math.sin(angle2)
    
    return [(x1, y1), (x2, y2)]

if not line_intersects_circle(ax, ay, bx, by, r):
    result = math.sqrt((bx-ax)**2 + (by-ay)**2)
else:
    tangents_A = find_tangent_points(ax, ay, r)
    tangents_B = find_tangent_points(bx, by, r)
    
    min_path = float('inf')
    
    for ta in tangents_A:
        for tb in tangents_B:
            distA = math.sqrt((ax - ta[0])**2 + (ay - ta[1])**2)
            distB = math.sqrt((bx - tb[0])**2 + (by - tb[1])**2)
            
            angle_a = math.atan2(ta[1], ta[0])
            angle_b = math.atan2(tb[1], tb[0])
            
            if angle_a < 0:
                angle_a += 2*math.pi
            if angle_b < 0:
                angle_b += 2*math.pi
            
            diff = abs(angle_a - angle_b)
            if diff > math.pi:
                diff = 2*math.pi - diff
            
            arc_length = r * diff
            
            total = distA + distB + arc_length
            min_path = min(min_path, total)
    
    result = min_path

print(f"{result:.10f}")