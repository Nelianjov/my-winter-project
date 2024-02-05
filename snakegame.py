import pygame
import random

pygame.init()
pygame.display.set_caption("Winter Project")   # sets the title at the top of the window

# dimensions of the window
width = 500
height = 500

# COLOURS
red = (255, 0, 0)
green = (0, 150, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode((width, height))

# coordinates of the snake
snake_x = 0
snake_y = 0
sides = 10  # the sides of rectangle

# coordinates of the fruit
fruit_x = 250
fruit_y = 250

# velocity/direction of the snake
vel_x = 10
vel_y = 0
score = 0

clock = pygame.time.Clock()

# FUNCTIONS WILL GO HERE

# game loop starts here
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # when user presses a key on the kbd
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                if snake_x <= width - sides:
                    if not (vel_y == 0):
                        if vel_x < 0:  # if the direction is negative such that to the left, make it go to the right
                            vel_x = -vel_x
                        else:
                            vel_x = 10  # if the direction is positive such that to the right, leave it the way it is
                            # pass just means do nothing
                        vel_y = 0
            if event.key == pygame.K_LEFT:
                if not (vel_y == 0):
                    if snake_x >= 0:
                        if vel_x > 0:  # if direction is positive ie going to the right, then make
                            # #it negative to go to the
                            # #left
                            vel_x = -vel_x
                        else:
                            vel_x = -10  # if the direction is negative already ie going to the left, do nothing
                        vel_y = 0

            if not (vel_x == 0):
                if event.key == pygame.K_UP:
                    if snake_y >= 0:
                        if vel_y > 0:
                            vel_y = -vel_y
                        else:
                            vel_y = -10
                        vel_x = 0
                if event.key == pygame.K_DOWN:
                    if snake_y <= height - sides:
                        if vel_y < 0:
                            vel_y = -vel_y
                        else:
                            vel_y = 10
                        vel_x = 0

    snake_x += vel_x
    snake_y += vel_y
    clock.tick(10)
    screen.fill(green)
    fruit = pygame.draw.rect(screen, blue, pygame.Rect(fruit_x, fruit_y, sides, sides))
    snake = pygame.draw.rect(screen, blue, pygame.Rect(snake_x, snake_y, sides, sides))
    collide = pygame.Rect.colliderect(snake,fruit)
    if collide:  # generating the rect at a random position when you click d
        fruit_x = random.randint(0, 400)
        fruit_y = random.randint(0, 400)
        score = score + 1
    font = pygame.font.SysFont('freesans.ttf', 20)
    text = font.render('score = {0}'.format(score), True, (255, 255, 255), green)
    text_container = text.get_rect()
    text_container.center = (30, 30)
    screen.blit(text, text_container)
    pygame.display.update()

    if snake_x < 0 or snake_x > width - sides or snake_y < 0 or snake_y > width - sides:
        # game over
        running = False
print(score)
pygame.quit()
