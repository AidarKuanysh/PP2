import pygame
import math

def draw_rect(surface, color, start, end, width=0):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    w = abs(start[0] - end[0])
    h = abs(start[1] - end[1])
    if w > 0 and h > 0:
        pygame.draw.rect(surface, color, (x, y, w, h), width)

def draw_square(surface, color, start, end, width=0):
    w = abs(start[0] - end[0])
    h = abs(start[1] - end[1])
    side = max(w, h)
    x = start[0] if end[0] > start[0] else start[0] - side
    y = start[1] if end[1] > start[1] else start[1] - side
    pygame.draw.rect(surface, color, (x, y, side, side), width)

def draw_circle(surface, color, start, end, width=0):
    x_dist = end[0] - start[0]
    y_dist = end[1] - start[1]
    radius = int((x_dist**2 + y_dist**2)**0.5)
    if radius > 0:
        safe_width = min(width, radius)
        pygame.draw.circle(surface, color, start, radius, safe_width)

def draw_right_triangle(surface, color, start, end, width=0):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surface, color, points, width)

def draw_equilateral_triangle(surface, color, start, end, width=0):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    side = int((dx**2 + dy**2)**0.5)
    height = int(side * math.sqrt(3) / 2)
    
    if end[1] < start[1]: height = -height
    
    p1 = start
    p2 = (start[0] + side, start[1])
    p3 = (start[0] + side // 2, start[1] - height)
    
    pygame.draw.polygon(surface, color, [p1, p2, p3], width)

def draw_rhombus(surface, color, start, end, width=0):
    mid_x = (start[0] + end[0]) // 2
    mid_y = (start[1] + end[1]) // 2
    
    p1 = (mid_x, start[1])
    p2 = (end[0], mid_y)
    p3 = (mid_x, end[1])
    p4 = (start[0], mid_y)
    
    pygame.draw.polygon(surface, color, [p1, p2, p3, p4], width)

def flood_fill(surface, pos, fill_color):
    target_color = surface.get_at(pos)
    if target_color == fill_color:
        return
    
    width, height = surface.get_size()
    stack = [pos]
    
    while stack:
        x, y = stack.pop()

        x1 = x
        while x1 > 0 and surface.get_at((x1 - 1, y)) == target_color:
            x1 -= 1

        x2 = x
        while x2 < width - 1 and surface.get_at((x2 + 1, y)) == target_color:
            x2 += 1
            
        for i in range(x1, x2 + 1):
            surface.set_at((i, y), fill_color)
            if y > 0 and surface.get_at((i, y - 1)) == target_color:
                stack.append((i, y - 1))
            if y < height - 1 and surface.get_at((i, y + 1)) == target_color:
                stack.append((i, y + 1))

def draw_ui(screen, tool, color, size):
    font = pygame.font.SysFont("Arial", 16)
    
    ui_bg = pygame.Surface((800, 50))
    ui_bg.fill((230, 230, 230))
    screen.blit(ui_bg, (0, 550))
    
    text1 = font.render(f"Tool: {tool.capitalize()} | Size: {size}px | Color: 1-4 | Ctrl+S: Save", True, (30, 30, 30))
    text2 = font.render("Keys: P(encil), L(ine), F(ill), A(Text), R(ect), C(irc), S(quar), T(Right), G(Equi), H(Rhomb), UP/DN(Size)", True, (80, 80, 80))
    
    screen.blit(text1, (10, 555))
    screen.blit(text2, (10, 575))