import pygame
import random
pygame.init()
width = 500
height = 500
sides = 10 # the sides of rectangle
green = (0,150,0)
blue = (0,0,255)
x = 250
y = 250
screen = pygame.display.set_mode((width, height))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:#generating the rect at a random position when you click d
                x = random.randint(0, 500)
                y = random.randint(0, 500)
    screen.fill((green))
    pygame.draw.rect(screen, (blue), pygame.Rect(x, y, sides,sides))# drawing the rect
    pygame.display.update()
pygame.quit()