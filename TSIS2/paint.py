import pygame
import datetime
import tools

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Extended Paint (TSIS 2)")
    
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE  = (0, 0, 255)

    active_color = BLACK
    active_tool = 'pencil'

    thicknesses = [2, 5, 10]
    thickness_idx = 0
    brush_size = thicknesses[thickness_idx]

    canvas = pygame.Surface((800, 600))
    canvas.fill(WHITE)
    
    drawing = False
    start_pos = None
    last_pos = None  

    text_mode = False
    current_text = ""
    text_pos = (0, 0)
    sys_font = pygame.font.SysFont("Arial", 24)

    while True:
        screen.fill((200, 200, 200))
        screen.blit(canvas, (0, 0)) 

        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if text_mode:
                    if event.key == pygame.K_RETURN:
                        text_surface = sys_font.render(current_text, True, active_color)
                        canvas.blit(text_surface, text_pos)
                        text_mode = False
                    elif event.key == pygame.K_ESCAPE:
                        text_mode = False
                    elif event.key == pygame.K_BACKSPACE:
                        current_text = current_text[:-1]
                    else:
                        current_text += event.unicode
                    continue 

                if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    filename = f"canvas_{timestamp}.png"
                    pygame.image.save(canvas, filename)
                    print(f"Canvas saved as {filename}")
                    continue 
                
                if event.key == pygame.K_p: active_tool = 'pencil'
                if event.key == pygame.K_l: active_tool = 'line'
                if event.key == pygame.K_f: active_tool = 'fill'
                if event.key == pygame.K_a: active_tool = 'text'
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

                if event.key == pygame.K_UP:
                    thickness_idx = min(len(thicknesses) - 1, thickness_idx + 1)
                    brush_size = thicknesses[thickness_idx]
                if event.key == pygame.K_DOWN:
                    thickness_idx = max(0, thickness_idx - 1)
                    brush_size = thicknesses[thickness_idx]

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if active_tool == 'text':
                        if not text_mode:
                            text_mode = True
                            text_pos = event.pos
                            current_text = ""
                    elif active_tool == 'fill':
                        tools.flood_fill(canvas, event.pos, active_color)
                    else:
                        drawing = True
                        start_pos = event.pos
                        last_pos = event.pos
            
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if active_tool == 'pencil':
                        pygame.draw.line(canvas, active_color, last_pos, event.pos, brush_size)
                        last_pos = event.pos
                    elif active_tool == 'brush':
                        pygame.draw.circle(canvas, active_color, event.pos, brush_size)
                    elif active_tool == 'eraser':
                        pygame.draw.circle(canvas, WHITE, event.pos, brush_size * 2)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    end_pos = event.pos
                    if active_tool == 'line':
                        pygame.draw.line(canvas, active_color, start_pos, end_pos, brush_size)
                    elif active_tool == 'rect':
                        tools.draw_rect(canvas, active_color, start_pos, end_pos, brush_size)
                    elif active_tool == 'circle':
                        tools.draw_circle(canvas, active_color, start_pos, end_pos, brush_size)
                    elif active_tool == 'square':
                        tools.draw_square(canvas, active_color, start_pos, end_pos, brush_size)
                    elif active_tool == 'right_triangle':
                        tools.draw_right_triangle(canvas, active_color, start_pos, end_pos, brush_size)
                    elif active_tool == 'equilateral_triangle':
                        tools.draw_equilateral_triangle(canvas, active_color, start_pos, end_pos, brush_size)
                    elif active_tool == 'rhombus':
                        tools.draw_rhombus(canvas, active_color, start_pos, end_pos, brush_size)

        if drawing:
            if active_tool == 'line':
                pygame.draw.line(screen, active_color, start_pos, mouse_pos, brush_size)
            elif active_tool == 'rect':
                tools.draw_rect(screen, active_color, start_pos, mouse_pos, brush_size)
            elif active_tool == 'circle':
                tools.draw_circle(screen, active_color, start_pos, mouse_pos, brush_size)
            elif active_tool == 'square':
                tools.draw_square(screen, active_color, start_pos, mouse_pos, brush_size)
            elif active_tool == 'right_triangle':
                tools.draw_right_triangle(screen, active_color, start_pos, mouse_pos, brush_size)
            elif active_tool == 'equilateral_triangle':
                tools.draw_equilateral_triangle(screen, active_color, start_pos, mouse_pos, brush_size)
            elif active_tool == 'rhombus':
                tools.draw_rhombus(screen, active_color, start_pos, mouse_pos, brush_size)

        if text_mode:
            text_surface = sys_font.render(current_text + "|", True, active_color)
            screen.blit(text_surface, text_pos)

        tools.draw_ui(screen, active_tool, active_color, brush_size)
        
        pygame.display.flip()
        clock.tick(120)

if __name__ == "__main__":
    main()