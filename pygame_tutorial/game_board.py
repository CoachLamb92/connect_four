import pygame

from pygame.locals import *


def game_board(width=800, height=800):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Morgan's Connect4")

    # Board-making maths
    units_per_width = (width-20)//22
    units_per_height = (height-20)//19
    magic_pixel_size = min([units_per_width, units_per_height])
    board_height = magic_pixel_size * 19
    board_width = magic_pixel_size * 22
    top_left_x = (width-board_width)//2
    top_left_y = (height-board_height)//2
    board = pygame.Rect(top_left_x, top_left_y, board_width, board_height)

    gameOn = True
    while gameOn:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    gameOn = False

                if event.key == K_1:
                    print("1 pressed")
                if event.key == K_2:
                    print("2 pressed")
                if event.key == K_3:
                    print("3 pressed")
                if event.key == K_4:
                    print("4 pressed")
                if event.key == K_5:
                    print("5 pressed")
                if event.key == K_6:
                    print("6 pressed")
                if event.key == K_7:
                    print("7 pressed")

            elif event.type == QUIT:
                gameOn = False
        
        pygame.draw.rect(screen, (0, 0, 255), board)
        for i in range(top_left_x + 2 * magic_pixel_size, top_left_x + board_width, 3 * magic_pixel_size):
            for j in range(top_left_y + 2 * magic_pixel_size, top_left_y + board_height, 3 * magic_pixel_size):
                pygame.draw.circle(screen, (255, 255, 255), (i, j), magic_pixel_size)

        pygame.display.update()

