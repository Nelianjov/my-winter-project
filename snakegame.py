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
white = (255, 255, 255)

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
score_file = open('scores.txt', 'r+')
high_score = int(score_file.readline().strip() or 0)
score_file.close()
score = 0

#text
font = pygame.font.SysFont('freesans.ttf', 20)
game_over_text = font.render('Game Over, Retry?', True, white, green)
game_over_bg = game_over_text.get_rect()
game_over_bg.center = (width//2, height//2)
score_text = font.render('Highscore: {0}  score: {1}'.format(high_score, score), True, (255, 255, 255), green)
score_border = score_text.get_rect()
score_border.center = (70, 20)

## open a file
score_file = open('scores.txt', 'w')
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
    text = font.render('high score: {0}  score = {1}'.format(high_score, score), True, (255, 255, 255), green)
    text_container = text.get_rect()
    text_container.center = (90, 30)
    screen.blit(text, text_container)
    pygame.display.update()

    if snake_x < 0 or snake_x > width - sides or snake_y < 0 or snake_y > width - sides:
        # game over
        # stop the game
        vel_x = 0
        vel_y = 0

        # print GAME OVER text
        screen.blit(game_over_text, game_over_bg)

        # check the highscore
        if score > high_score:
            # open("scores.txt", "w").close() # clear the file
            score_file.write(str(score))
            score_file.close()
        else:
            score_file.write(str(high_score))
            score_file.close()

        # game over
        screen.blit(score_text, score_border)
        pygame.display.update()
        running = False
pygame.quit()
