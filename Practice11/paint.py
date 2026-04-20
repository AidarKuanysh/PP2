import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Extended Paint")
    
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE  = (0, 0, 255)

    active_color = BLACK
    active_tool = 'brush'
    radius = 15

    canvas = pygame.Surface((800, 600))
    canvas.fill(WHITE)
    
    drawing = False
    start_pos = None

    while True:
        screen.fill((200, 200, 200))
        screen.blit(canvas, (0, 0)) 

        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    drawing = True
                    start_pos = event.pos
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = event.pos
                    if active_tool == 'rect':
                        draw_rect(canvas, active_color, start_pos, end_pos)
                    elif active_tool == 'circle':
                        draw_circle(canvas, active_color, start_pos, end_pos)
                    elif active_tool == 'square':
                        draw_square(canvas, active_color, start_pos, end_pos)
                    elif active_tool == 'right_triangle':
                        draw_right_triangle(canvas, active_color, start_pos, end_pos)
                    elif active_tool == 'equilateral_triangle':
                        draw_equilateral_triangle(canvas, active_color, start_pos, end_pos)
                    elif active_tool == 'rhombus':
                        draw_rhombus(canvas, active_color, start_pos, end_pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: active_tool = 'rect'
                if event.key == pygame.K_c: active_tool = 'circle'
                if event.key == pygame.K_b: active_tool = 'brush'
                if event.key == pygame.K_e: active_tool = 'eraser'
                if event.key == pygame.K_s: active_tool = 'square'
                if event.key == pygame.K_t: active_tool = 'right_triangle'
                if event.key == pygame.K_g: active_tool = 'equilateral_triangle'
                if event.key == pygame.K_h: active_tool = 'rhombus'
                
                if event.key == pygame.K_1: active_color = RED
                if event.key == pygame.K_2: active_color = GREEN
                if event.key == pygame.K_3: active_color = BLUE
                if event.key == pygame.K_4: active_color = BLACK

        if drawing:
            if active_tool == 'brush':
                pygame.draw.circle(canvas, active_color, mouse_pos, radius)
            elif active_tool == 'eraser':
                pygame.draw.circle(canvas, WHITE, mouse_pos, radius)
            elif active_tool == 'rect':
                draw_rect(screen, active_color, start_pos, mouse_pos, width=2)
            elif active_tool == 'circle':
                draw_circle(screen, active_color, start_pos, mouse_pos, width=2)
            elif active_tool == 'square':
                draw_square(screen, active_color, start_pos, mouse_pos, width=2)
            elif active_tool == 'right_triangle':
                draw_right_triangle(screen, active_color, start_pos, mouse_pos, width=2)
            elif active_tool == 'equilateral_triangle':
                draw_equilateral_triangle(screen, active_color, start_pos, mouse_pos, width=2)
            elif active_tool == 'rhombus':
                draw_rhombus(screen, active_color, start_pos, mouse_pos, width=2)

        draw_ui(screen, active_tool, active_color)
        
        pygame.display.flip()
        clock.tick(60)


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
        pygame.draw.circle(surface, color, start, radius, width)

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

def draw_ui(screen, tool, color):
    font = pygame.font.SysFont("Arial", 16)
    text = font.render(f"Tool: {tool.capitalize()} | Keys: R, C, B, E, S(Square), T(Right), G(Equi), H(Rhombus)", True, (50, 50, 50))
    screen.blit(text, (10, 575))

if __name__ == "__main__":
    main()