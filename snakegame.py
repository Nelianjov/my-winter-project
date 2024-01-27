import pygame
pygame.init()
width = 500
height = 500
green = (0,150,0)
blue = (0,0,255)
screen = pygame.display.set_mode((width, height))
running = True
while running:
    screen.fill((green))
    pygame.display.update()
pygame.quit()