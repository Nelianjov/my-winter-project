import pygame
import random
pygame.init()
pygame.display.set_caption("Winter Project") # sets the title at the top of the window
width = 500
height = 500

# COLOURS
red = (255, 0, 0)
green = (0, 150, 0)
blue = (0, 0, 255)
sides = 10 # the sides of rectangle

screen = pygame.display.set_mode((width, height))

# coordinates of the snake
snake_x = 0
snake_y = 0

# velocity/direction of the snake
vel_x = 10
vel_y = 0

# coordinates of the fruit
fruit_x = 250
fruit_y = 250


clock = pygame.time.Clock()

# beginning of the infinite loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: # generating the rect at a random position when you click d
                fruit_x = random.randint(0, width)
                fruit_y = random.randint(0, height)

            # adding the direction controls
            if event.type == pygame.KEYDOWN:

                # events for left and right
                if event.key == pygame.K_RIGHT:
                    if snake_x <= width / 2:
                        if vel_x < 0:  # if the direction is negaive i.e to the left, make it go to the right
                            vel_x = -vel_x
                        else:
                            vel_x = 10 # if the direction is positive i.e to the right, leave it the way it is
                                #pass just means do nothing
                        vel_y = 0
                if event.key == pygame.K_LEFT:
                    if snake_x >= 0:
                        if vel_x > 0: # if direction is positive i.e going to the right, then make it negative to go to the left
                            vel_x = -vel_x
                        else:
                            vel_x = -10# if the direction is negative already i.e going to the left, do nothing
                        vel_y = 0

                # events for up and down
                if event.key == pygame.K_UP:
                    if snake_y >= 0:
                        if vel_y > 0:
                            vel_y = -vel_y
                        else:
                            vel_y = -10
                        vel_x = 0
                if event.key == pygame.K_DOWN:
                    if snake_y <= height / 2:
                        if vel_y < 0:
                            vel_y = -vel_y
                        else:
                            vel_y = 10
                        vel_x = 0


    ## SNAKE CODE

    # declaring the snake variable
    snake_x += vel_x
    snake_y += vel_y
    clock.tick(3)
    screen.fill(green)
    pygame.draw.rect(screen, blue, pygame.Rect(fruit_x, fruit_y, sides, sides))
    snake = pygame.draw.rect(screen, blue, pygame.Rect(snake_x, snake_y, sides, sides))
    pygame.display.update()
pygame.quit()
