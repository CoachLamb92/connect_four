class ConnectFourGame:
    def __init__(self):
        self._new_board = [
            ["_", "_", "_", "_", "_", "_", "_"],    # row 0
            ["_", "_", "_", "_", "_", "_", "_"],    # row 1
            ["_", "_", "_", "_", "_", "_", "_"],    # row 2
            ["_", "_", "_", "_", "_", "_", "_"],    # row 3
            ["_", "_", "_", "_", "_", "_", "_"],    # row 4
            ["_", "_", "_", "_", "_", "_", "_"]     # row 5
        ]
        self._current_board = self._new_board
        self._turn_count = 1
        self._active_board = True

    def play(self, column_to_drop):
        if not self._active_board:
            print("""The game is over! Please begin a new game by typing:
new_game = ConnectFourGame()
Alternatively, leave now and never come back by typing:
exit()""")
            return
        if self._current_board[0][column_to_drop-1] != "_":
            print("This column is full! Please pick another.")
            return
        else:
            last_free_slot = 0
            for i in range(1, 6):
                if self._current_board[i][column_to_drop-1] != "_":
                    break
                else:
                    last_free_slot = i
        self.update_board(last_free_slot, column_to_drop-1)
        self.increment_turn_counter()
        for row in self._current_board:
            print(row)
        result = self.check_winner()
        if result:
            self._active_board = False
            return result + " is the winner!"
        return

    def update_board(self, row, column):
        self._current_board[row][column] = self.get_player()

    def increment_turn_counter(self):
        self._turn_count += 1

    def get_turn_count(self):
        return self._turn_count

    def get_board(self):
        return self._current_board

    def get_player(self):
        return "X" if self.get_turn_count() % 2 == 1 else "O"

    def check_winner(self):
        rows = 6
        columns = 7
        x_win = ["X", "X", "X", "X"]
        o_win = ["O", "O", "O", "O"]
        # row check
        for i in range(rows):
            for j in range(columns-3):
                if self._current_board[i][j:j+4] == x_win:
                    return "X"
                elif self._current_board[i][j:j+4] == o_win:
                    return "O"

        # column check
        for i in range(columns):
            for j in range(rows-3):
                check_list = [self._current_board[j+k][i] for k in range(4)]
                # print(check_list)
                if check_list == x_win:
                    return "X"
                elif check_list == o_win:
                    return "O"

        # positive correlation diagonal check
        for i in range(rows):
            for j in range(columns):
                if self._current_board[i][j] == "_":
                    continue
                try:
                    check_list = [self._current_board[i+n][j+n]
                                  for n in range(4)]
                    if check_list == x_win:
                        return "X"
                    elif check_list == o_win:
                        return "O"
                    else:
                        raise Exception
                except Exception:
                    try:
                        check_list = [self._current_board[i+n][j-n]
                                      for n in range(4)]
                        if check_list == x_win:
                            return "X"
                        elif check_list == o_win:
                            return "O"
                    except Exception:
                        continue
        return False

    def available_slots(self):
        slots = [str(i+1) for i in range(len(
            self._current_board[0])) if self._current_board[0][i] == '_']
        if len(slots) > 1:
            output = ', '.join(slots[:-1]) + " or " + slots[-1]
        elif len(slots) == 1:
            output = slots[0]
        else:
            output = "draw"
        return output