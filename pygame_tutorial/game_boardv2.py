import pygame
from src.main import game_state
from pygame.locals import *


def game_board(width=800, height=800, p1_name="", p2_name=""):
    p1_name = "Player 1" if not p1_name else p1_name
    p2_name = "Player 2" if not p2_name else p2_name
    pygame.init()
    board_state = [
            ["X", "X", "X", "_", "O", "O", "O"],    # row 0
            ["X", "_", "X", "_", "_", "O", "_"],    # row 1
            ["X", "X", "X", "_", "_", "O", "_"],    # row 2
            ["X", "_", "X", "_", "_", "O", "_"],    # row 3
            ["X", "_", "X", "_", "_", "O", "_"],    # row 4
            ["X", "_", "X", "_", "O", "O", "O"]     # row 5
        ]
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
    
    muted_white = (200, 200, 200)
    muted_red = (200, 0, 0)
    muted_yellow = (200, 200, 0)
    muted_blue = (0, 0, 200)

    gameOn = True
    while gameOn:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
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
        
        pygame.draw.rect(screen, muted_blue, board)
        for i in range(len(board_state)):
            for j in range(len(board_state[i])):
                x_coord = top_left_x + (magic_pixel_size * (2 + (3 * j)))
                y_coord = top_left_y + (magic_pixel_size * (2 + (3 * i)))
                if board_state[i][j] == "_":
                    circle_colour = muted_white
                elif board_state[i][j] == "X":
                    circle_colour = muted_red
                else:
                    circle_colour = muted_yellow
                pygame.draw.circle(screen, circle_colour, (x_coord, y_coord), magic_pixel_size)

        pygame.display.update()

# game_board()