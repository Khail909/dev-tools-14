import pygame
 
pygame.init()
 
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255,100,10)
 
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Dream team')
 
game_over = False
 
x = 150
y = 150
 
x_change = 0       
y_change = 0
 
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 5
                x_change = 0
            elif event.key == pygame.K_LEFT:
                x_change = -5
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 5
                y_change = 0
 
    x += x_change
    y += y_change
    dis.fill(GREEN)
    pygame.draw.rect(dis, ORANGE, [x, y, 5, 5])
 
    pygame.display.update()
 
    clock.tick(20)
 
pygame.quit()
quit()