import pygame
pygame.init()
pygame.display.set_caption("Winter Project") # sets the title at the top of the window
width = 500
height = 500
green = (0,150,0)
blue = (0,0,255)
screen = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
    screen.fill((green))
    pygame.display.update()
pygame.quit()