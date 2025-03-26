from src.utils import ConnectFourGame

def game_state(p1, p2):
    print("Welcome to Connect Four!")
    # player_1 = input("Enter a name for player 1:\n")
    # player_2 = input("Enter a name for player 2:\n")
    new_game = ConnectFourGame()
    while True:
        if new_game.check_winner(): break
        current_player = p1 if new_game.get_player() == "X" else p2
        print(f'{current_player}, it\'s your go now, place your {new_game.get_player()}!')
        turn  = input("Input a column number from 1 (left) to 7 (right) to place your token\n")
        while turn not in [str(num) for num in range(1, 7)]:
            print("Invalid choice")
            turn  = input("Please input a column number from 1 (left) to 7 (right) to place your token\n")
        new_game.play(int(turn)-1)
    print(f"{current_player} won the game!")


# game_state()
