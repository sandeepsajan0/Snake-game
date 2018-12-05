import pygame
import random
import os

os.chdir('mainfiles')

#from static.colors import white, red, black, green

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
block_size = 10

clock = pygame.time.Clock()
FPS = 18
background_image = pygame.image.load("static/snake.png")
pause_image = pygame.image.load("static/pause.jpg")

font = pygame.font.SysFont(None, 35)
font_large = pygame.font.SysFont(None, 75)


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        gameDisplay.blit(pause_image, [280, 35])
        message_to_screen("Paused", red, 20, 'L')
        message_to_screen("Press r for Resume and q for Quit", red, 90, 's')
        pygame.display.update()


def update_score(score):
    text = font.render("SCORE:{score}", True, black)
    gameDisplay.blit(text, [0, 0])


def shortcuts():
    welcome_screen = True
    while welcome_screen:
        welcome_screen = handle_key_on_welcome_screen()
        gameDisplay.fill(white)
        message_to_screen("Shortcuts for snake game", green, -200, 'L')
        message_to_screen("Play -> p", black, -100, 's')
        message_to_screen("Quit -> q", black, -55, 's')
        message_to_screen("Pause -> b", black, 80, 's')
        message_to_screen("Resume -> r", black, 125, 's')
        message_to_screen("Back -> e", black, -10, 's')
        message_to_screen("Shortcuts -> s", black, 170, 's')
        message_to_screen("Home -> h", black, 35, 's')
        pygame.display.update()


def handle_key_on_welcome_screen() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                intro()
                return False
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.key == pygame.K_h:
                intro()
                return False
    return True


def intro():
    intro = True
    while intro:
        intro = handle_key_during_game()
        gameDisplay.blit(background_image, [85, 50])
        # gameDisplay.fill(white)
        message_to_screen("Welcome to snake game", green, -200, 'L')
        message_to_screen("Press q for Quit", black, -100, 's')
        message_to_screen("Press p for Play", black, -50, 's')
        message_to_screen("Press s for Shortcuts", black, 0, 's')
        pygame.display.update()


def handle_key_during_game() -> bool:
    gameDisplay.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_loop()
                return False
            elif event.key == pygame.K_q:
                pygame.quit()
                quit()
                return False
            elif event.key == pygame.K_s:
                shortcuts()
                return False
    return True


def text_objects(text, color, size):
    if size == "L":
        text_surface = font_large.render(text, True, color)
    else:
        text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_to_screen(msg, color, y_displace, size):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(text_surf, text_rect)


def snake_create(block_size, snake_list):
    for el in snake_list:
        pygame.draw.rect(gameDisplay, green, [el[0], el[1], block_size, block_size])


def game_loop():
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    snake_list = []
    snake_length = 1
    lead_x_change = 0
    lead_y_change = 0
    randappleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    randappleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
    while not gameExit:
        if gameOver:
            message_to_screen("Game over", red, -200, 'L')
            message_to_screen("Press p for Play again!", black, -100, 's')
            message_to_screen("Press q for Quit!", black, -50, 's')
            message_to_screen("Press h for Home!", black, 0, 's')
            pygame.display.update()
        while gameOver:
            # gameDisplay.blit(background_image, [0, 0])
            # gameDisplay.fill(sky_blue)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    if event.key == pygame.K_h:
                        intro()
                    if event.key == pygame.K_p:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    # print lead_x
                    lead_y_change = 0
                # lead_x -=10
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    # print lead_x
                    lead_y_change = 0
                # lead_x += 10
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                # lead_y -=10
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                # lead_y += 10
                elif event.key == pygame.K_b:
                    pause()
        if lead_x <= 0 or lead_y <= 0 or lead_x >= display_width or lead_y >= display_height:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        # gameDisplay.blit(background_image, [0, 0])
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randappleX, randappleY, block_size, block_size])
        # print randappleX,randappleY,lead_x,lead_y
        snake_create(block_size, snake_list)
        update_score(snake_length - 1)
        pygame.display.update()

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snake_list.append(snakehead)
        if snake_length < len(snake_list):
            del (snake_list[0])

        if lead_x == randappleX and lead_y == randappleY:
            randappleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            randappleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            # print randappleY,randappleY + block_size,lead_y
            # print randappleX,randappleY,lead_x,lead_y
            snake_length += 1

        clock.tick(FPS)

    pygame.quit()
    quit()


intro()
