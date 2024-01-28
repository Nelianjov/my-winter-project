import pygame
import random
pygame.init()
pygame.display.set_caption("Winter Project") # sets the title at the top of the window
width = 500
height = 500
green = (0, 150, 0)
blue = (0, 0, 255)
screen = pygame.display.set_mode((width, height))

# snake
snake_x_pos = 0
snake_y_pos = 0
block_size = 30
vel = 1
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
    if snake_x_pos <= width:
        snake_x_pos += vel
        clock.tick(2)

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         if snake_x_pos <= width/2:
        #             snake_x_pos += vel
        #     if event.key == pygame.K_LEFT:
        #         if snake_x_pos >= 0:
        #             snake_x_pos -= vel
        #
        #     if event.key == pygame.K_UP:
        #         if snake_y_pos >= 0:
        #             snake_y_pos -= vel
        #     if event.key == pygame.K_DOWN:
        #         if snake_y_pos <= height/2:
        #             snake_y_pos += vel
                # add a boundary
    screen.fill(green)
    snake = pygame.draw.rect(screen, blue, pygame.Rect(snake_x_pos, snake_y_pos, block_size, block_size))
    pygame.display.update()
pygame.quit()
