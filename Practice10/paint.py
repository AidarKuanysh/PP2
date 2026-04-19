import pygame

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: active_tool = 'rect'
                if event.key == pygame.K_c: active_tool = 'circle'
                if event.key == pygame.K_b: active_tool = 'brush'
                if event.key == pygame.K_e: active_tool = 'eraser'
                # Colors
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

def draw_circle(surface, color, start, end, width=0):
    x_dist = end[0] - start[0]
    y_dist = end[1] - start[1]
    radius = int((x_dist**2 + y_dist**2)**0.5)
    if radius > 0:
        pygame.draw.circle(surface, color, start, radius, width)

def draw_ui(screen, tool, color):
    font = pygame.font.SysFont("Arial", 18)
    text = font.render(f"Tool: {tool.capitalize()} | Color: {color} (Keys: R, C, B, E | 1, 2, 3, 4)", True, (50, 50, 50))
    screen.blit(text, (10, 570))

if __name__ == "__main__":
    main()