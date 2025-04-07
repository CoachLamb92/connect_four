import pygame
from pygame.locals import K_1, K_2, K_3, K_4, K_5, K_6, K_7
from pygame.locals import KEYDOWN, K_ESCAPE, QUIT
from src.utils import ConnectFourGame


def game_board(width=800, height=800, p1_name="", p2_name=""):
    p1_name = "Player 1" if not p1_name else p1_name
    p2_name = "Player 2" if not p2_name else p2_name
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Morgan's Connect4")

    # Board-making maths
    units_per_width = (width-20)//22
    units_per_height = (height-40)//19
    magic_pixel_size = min([units_per_width, units_per_height])
    board_height = magic_pixel_size * 19
    board_width = magic_pixel_size * 22
    top_left_x = (width-board_width)//2
    top_left_y = (height-board_height)//2
    board = pygame.Rect(top_left_x, top_left_y, board_width, board_height)

    game_text_rect = pygame.Rect(board.x, 0, board_width, 70)

    # colours
    white = (255, 255, 255)
    muted_white = (200, 200, 200)
    muted_red = (200, 0, 0)
    muted_yellow = (200, 200, 0)
    muted_blue = (0, 0, 200)

    # fonts
    smallfont = pygame.font.SysFont('Corbel', 35)

    # texts
    p1_text = f'{p1_name}, it\'s your turn! (you are red)'
    p2_text = f'{p2_name}, it\'s your turn! (you are yellow)'

    narrator_text = smallfont.render(p1_text, True, white)

    gameOn = True
    new_game = ConnectFourGame()
    board_state = new_game.get_board()

    while gameOn:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    gameOn = False

                if event.key in [K_1, K_2, K_3, K_4, K_5, K_6, K_7]:
                    if event.key == K_1:
                        new_game.play(1)
                    if event.key == K_2:
                        new_game.play(2)
                    if event.key == K_3:
                        new_game.play(3)
                    if event.key == K_4:
                        new_game.play(4)
                    if event.key == K_5:
                        new_game.play(5)
                    if event.key == K_6:
                        new_game.play(6)
                    if event.key == K_7:
                        new_game.play(7)
                    board_state = new_game.get_board()
                    if new_game.get_player() == "X":
                        narrator_text = smallfont.render(p1_text, True, white)
                    else:
                        narrator_text = smallfont.render(p2_text, True, white)
                else:
                    print("Please enter 1-7 to select the corresponding row")
                    print(reminder_text)
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
                pygame.draw.circle(screen, circle_colour,
                                   (x_coord, y_coord), magic_pixel_size)

        # Check winner of the match
        result = new_game.check_winner()
        if result == 'X':
            narrator_text = smallfont.render(
                f'{p1_name} wins! Press Esc to exit', True, white)
        elif result == 'O':
            narrator_text = smallfont.render(
                f'{p2_name} wins! Press Esc to exit', True, white)
        
        # Check which columns are left:
        result_2 = new_game.available_slots()
        if result_2 == 'draw':
            narrator_text = smallfont.render(
                f'A draw!!', True, white)
            reminder_text = smallfont.render(
                'Play again to discover who is the best!', True, white)
        else:
            reminder_text = smallfont.render(
                'Please choose from columns: ' + result_2, True, white)


        pygame.draw.rect(screen, muted_blue, game_text_rect)
        screen.blit(narrator_text, (game_text_rect.x+7, game_text_rect.y+7))
        screen.blit(reminder_text, (game_text_rect.x+7, game_text_rect.y+42))
        pygame.display.update()
