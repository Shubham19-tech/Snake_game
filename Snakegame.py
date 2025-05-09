import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display size
width = 600
height = 400

# Snake block and speed
block_size = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

# Create window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by Shubh 🐍')

# Clock
clock = pygame.time.Clock()

# Score
def show_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    win.blit(value, [0, 0])

# Snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, black, [x[0], x[1], snake_block, snake_block])

# Message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

# Game loop
def gameLoop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_List = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            win.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        win.fill(white)
        pygame.draw.rect(win, green, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)

        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for block in snake_List[:-1]:
            if block == snake_Head:
                game_close = True

        draw_snake(block_size, snake_List)
        show_score(length_of_snake - 1)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
