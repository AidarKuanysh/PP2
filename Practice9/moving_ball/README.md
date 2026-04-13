### 3.3 Moving Ball Game

**Objective**: Create an interactive game with a moving red ball

**Requirements**:
1. Display a red ball (50x50 pixels, radius 25) on white background
2. Move ball with arrow keys (Up, Down, Left, Right)
3. Each key press moves ball by 20 pixels
4. Ball cannot leave the screen boundaries
5. Ignore input that would move ball off-screen

**Implementation Tips**:
- Use pygame.draw.circle() for the ball
- Handle keyboard events
- Check boundary conditions before moving
- Smooth animation with frame rate control

**Repository Structure**:
```
Practice7/
├── moving_ball/
│   ├── main.py
│   ├── ball.py
│   └── README.md
```