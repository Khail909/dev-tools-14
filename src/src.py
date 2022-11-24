import pygame
import time
import random
 
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
 
dis = pygame.display.set_mode((1440, 1080))
pygame.display.set_caption('Dream team')
 
clock = pygame.time.Clock()
 
snake = 20
snake_speed = 15
 
font_style = pygame.font.SysFont(None, 30)
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [1440/3, 1080/3])
 
 
def gameLoop():  # creating a function
    close = False
    over = False
 
    x = 1440 / 2
    y = 1080 / 2
 
    foodx = round(random.randrange(0, 1440 - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, 1080 - snake) / 10.0) * 10.0
    xc = 0
    yc = 0
 
    while not over:
 
        while close == True:
            dis.fill(GREEN)
            message("Game over! 'r' - restart, q - 'quit'", BLACK)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_й:
                        over = True
                        close = False
                    if event.key == pygame.K_r or event.key == pygame.K_к:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    yc = -snake
                    xc = 0
                elif event.key == pygame.K_DOWN:
                    yc = snake
                    xc = 0
                elif event.key == pygame.K_LEFT:
                    xc = -snake
                    yc = 0
                elif event.key == pygame.K_RIGHT:
                    xc = snake
                    yc = 0
        x+=xc
        y+=yc
 
        if x >= 1440 or x < 0 or y >= 1080 or y < 0:
            close = True

        dis.fill(GREEN)
        pygame.draw.rect(dis, RED, [foodx, foody, snake, snake])
        pygame.draw.rect(dis, YELLOW, [x, y, snake, snake])
        pygame.display.update()
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()