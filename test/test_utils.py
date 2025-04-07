from src.utils import ConnectFourGame
import pytest
import io
import sys

@pytest.mark.skip
class TestInitMethod:
    def test_method_exists(self):
        # Arrange
        expected = "__init__"
        # Act
        result = dir(ConnectFourGame)
        # Assert
        assert expected in result

    def test_board_initialises_board_correctly(self):
        # Arrange
        expected = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"]
        ]
        # Act
        dummy_game = ConnectFourGame()
        result = dummy_game._current_board
        # Assert
        assert expected == result

    def test_board_initialises_turn_count_correctly(self):
        # Arrange
        expected = 1
        # Act
        dummy_game = ConnectFourGame()
        result = dummy_game._turn_count
        # Assert
        assert expected == result

@pytest.mark.skip
class TestPlayMethod:
    def test_method_exists(self):
        # Arrange
        expected = "play"
        # Act
        result = dir(ConnectFourGame)
        # Assert
        assert expected in result

    def test_method_returns_first_move_correctly(self):
        # Arrange
        expected_turn = 2
        expected_board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "X", "_", "_", "_"]
        ]
        expected_player = "O"
        # Act
        dummy_game = ConnectFourGame()
        dummy_game.play(3)
        result_board = dummy_game.get_board()
        result_turn = dummy_game.get_turn_count()
        result_player = dummy_game.get_player()
        # Assert
        assert expected_board == result_board
        assert expected_turn == result_turn
        assert expected_player == result_player

    def test_method_returns_first_two_moves_correctly_h(self):
        # Arrange
        expected_turn = 3
        expected_board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "X", "O", "_", "_"]
        ]
        expected_player = "X"
        # Act
        dummy_game = ConnectFourGame()
        dummy_game.play(3)
        dummy_game.play(4)
        result_board = dummy_game.get_board()
        result_turn = dummy_game.get_turn_count()
        result_player = dummy_game.get_player()
        # Assert
        assert expected_board == result_board
        assert expected_turn == result_turn
        assert expected_player == result_player

    def test_method_returns_first_two_moves_correctly_v(self):
        # Arrange
        expected_turn = 3
        expected_board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "O", "_", "_", "_"],
            ["_", "_", "_", "X", "_", "_", "_"]
        ]
        expected_player = "X"
        # Act
        dummy_game = ConnectFourGame()
        dummy_game.play(3)
        dummy_game.play(3)
        result_board = dummy_game.get_board()
        result_turn = dummy_game.get_turn_count()
        result_player = dummy_game.get_player()
        # Assert
        assert expected_board == result_board
        assert expected_turn == result_turn
        assert expected_player == result_player

    def test_method_does_not_progress_when_column_error(self):
        # Arrange
        expected_turn_before_error = 7
        expected_turn_after_error = 7
        expected_board_before_error = [
            ["O", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["O", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["O", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"]
        ]
        expected_board_after_error = [
            ["O", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["O", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["O", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"]
        ]
        expected_player_before_error = "X"
        expected_player_after_error = "X"
        # Act
        dummy_game = ConnectFourGame()
        dummy_game.play(0)
        dummy_game.play(0)
        dummy_game.play(0)
        dummy_game.play(0)
        dummy_game.play(0)
        dummy_game.play(0)
        result_board_before_error = dummy_game.get_board()
        result_turn_before_error = dummy_game.get_turn_count()
        result_player_before_error = dummy_game.get_player()
        dummy_game.play(0)
        result_board_after_error = dummy_game.get_board()
        result_turn_after_error = dummy_game.get_turn_count()
        result_player_after_error = dummy_game.get_player()
        # Assert
        assert expected_board_before_error == result_board_before_error
        assert expected_board_before_error == result_board_after_error
        assert expected_turn_before_error == result_turn_before_error
        assert expected_turn_after_error == result_turn_after_error
        assert expected_player_before_error == result_player_before_error
        assert expected_player_after_error == result_player_after_error
    
    def test_method_prints_error_message(self):
        # Arrange
        expected = "This column is full! Please pick another.\n"
        # Act
        dummy_game = ConnectFourGame()
        dummy_game.play(0)
        dummy_game.play(0)
        dummy_game.play(0)
        dummy_game.play(0)
        dummy_game.play(0)
        dummy_game.play(0)
        print_statement = io.StringIO()
        sys.stdout = print_statement
        dummy_game.play(0)
        sys.stdout = sys.__stdout__
        result = print_statement.getvalue()
        # Assert
        assert expected == result

@pytest.mark.skip
class TestUpdateBoardMethod:
    def test_method_exists(self):
        # Arrange
        expected = "update_board"
        # Act
        result = dir(ConnectFourGame)
        # Assert
        assert expected in result

    def test_method_returns_first_X_correctly(self):
        # Arrange
        expected = [
            ["X", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"]
        ]
        # Act
        dummy_game = ConnectFourGame()
        dummy_game.update_board(0, 0)
        result = dummy_game.get_board()
        # Assert
        assert expected == result

    def test_method_returns_first_O_correctly(self):
        # Arrange
        expected = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "O", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"]
        ]
        # Act
        dummy_game = ConnectFourGame()
        dummy_game.increment_turn_counter()
        dummy_game.update_board(2, 1)
        result = dummy_game.get_board()
        # Assert
        assert expected == result

    def test_method_returns_first_two_moves_correctly(self):
        # Arrange
        expected = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "O"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "X", "_", "_"]
        ]
        # Act
        dummy_game = ConnectFourGame()
        dummy_game.update_board(5, 4)
        dummy_game.increment_turn_counter()
        dummy_game.update_board(1, 6)
        result = dummy_game.get_board()
        # Assert
        assert expected == result

    def test_method_returns_first_four_moves_correctly(self):
        # Arrange
        expected = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "O"],
            ["O", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "X", "_"],
            ["_", "_", "_", "_", "X", "_", "_"]
        ]
        # Act
        dummy_game = ConnectFourGame()
        dummy_game.update_board(5, 4)
        dummy_game.increment_turn_counter()
        dummy_game.update_board(1, 6)
        dummy_game.increment_turn_counter()
        dummy_game.update_board(4, 5)
        dummy_game.increment_turn_counter()
        dummy_game.update_board(2, 0)
        result = dummy_game.get_board()
        # Assert
        assert expected == result

@pytest.mark.skip
class TestIncrementTurnCounterMethod:
    def test_method_exists(self):
        # Arrange
        expected = "increment_turn_counter"
        # Act
        result = dir(ConnectFourGame)
        # Assert
        assert expected in result

    def test_method_returns_correctly(self):
        # Arrange
        expected_first = 1
        expected_second = 2
        dummy_game = ConnectFourGame()
        result_first = dummy_game._turn_count
        dummy_game.increment_turn_counter()
        result_second = dummy_game._turn_count
        # Assert
        assert expected_first == result_first
        assert expected_second == result_second

@pytest.mark.skip
class TestGetTurnCountMethod:
    def test_method_exists(self):
        # Arrange
        expected = "get_turn_count"
        # Act
        result = dir(ConnectFourGame)
        # Assert
        assert expected in result

    def test_method_returns_correctly(self):
        # Arrange
        expected_first = 1
        expected_second = 2
        dummy_game = ConnectFourGame()
        result_first = dummy_game.get_turn_count()
        dummy_game.increment_turn_counter()
        result_second = dummy_game.get_turn_count()
        # Assert
        assert expected_first == result_first
        assert expected_second == result_second

@pytest.mark.skip
class TestGetBoardMethod:
    def test_method_exists(self):
        # Arrange
        expected = "get_board"
        # Act
        result = dir(ConnectFourGame)
        # Assert
        assert expected in result

    def test_board_initialises_board_correctly(self):
        # Arrange
        expected = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"]
        ]
        # Act
        dummy_game = ConnectFourGame()
        result = dummy_game.get_board()
        # Assert
        assert expected == result

@pytest.mark.skip
class TestGetPlayerMethod:
    def test_method_exists(self):
        # Arrange
        expected = "get_player"
        # Act
        result = dir(ConnectFourGame)
        # Assert
        assert expected in result

    def test_method_returns_X_correctly(self):
        # Arrange
        expected_first = "X"
        expected_third = "X"
        # Act
        dummy_game = ConnectFourGame()
        result_first = dummy_game.get_player()
        dummy_game.increment_turn_counter()
        dummy_game.increment_turn_counter()
        result_third = dummy_game.get_player()
        # Assert
        assert expected_first == result_first
        assert expected_third == result_third
    
    def test_method_returns_O_correctly(self):
        # Arrange
        expected_second = "O"
        expected_fourth = "O"
        # Act
        dummy_game = ConnectFourGame()
        dummy_game.increment_turn_counter()
        result_second = dummy_game.get_player()
        dummy_game.increment_turn_counter()
        dummy_game.increment_turn_counter()
        result_fourth = dummy_game.get_player()
        # Assert
        assert expected_second == result_second
        assert expected_fourth == result_fourth

@pytest.mark.skip
class TestCheckWinnerMethod:
    def test_method_exists(self):
        # Arrange
        expected = "check_winner"
        # Act
        result = dir(ConnectFourGame)
        # Assert
        assert expected in result

    def test_method_returns_winner_horizontal(self):
        # Arrange
        expected = "X"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "X", "X", "X", "X"]
        ]
        result = dummy_grid.check_winner()
        # Assert
        assert expected == result

        # Arrange
        expected = "O"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "O", "O", "O", "O", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"]
        ]
        result = dummy_grid.check_winner()
        # Assert
        assert expected == result
        
    def test_method_returns_winner_vertical(self):
        # Arrange
        expected = "X"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "X", "_", "_", "_"],
            ["_", "_", "_", "X", "_", "_", "_"],
            ["_", "_", "_", "X", "_", "_", "_"],
            ["_", "_", "_", "X", "_", "_", "_"]
        ]
        result = dummy_grid.check_winner()
        # Assert
        assert expected == result

        # Arrange
        expected = "O"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "_", "_", "_", "_", "O", "_"],
            ["_", "_", "_", "_", "_", "O", "_"],
            ["_", "_", "_", "_", "_", "O", "_"],
            ["_", "_", "_", "_", "_", "O", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"]
        ]
        result = dummy_grid.check_winner()
        # Assert
        assert expected == result

    def test_method_returns_x_winner_diagonal(self):
        # Arrange
        expected = "X"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "X", "_", "_", "_"],
            ["_", "_", "X", "_", "_", "_", "_"],
            ["_", "X", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"]
        ]
        result = dummy_grid.check_winner()
        # Assert
        assert expected == result

    def test_method_returns_x_winner_reverse_diagonal(self):
        # Arrange
        expected = "X"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "X", "_", "_", "_", "_", "_"],
            ["_", "_", "X", "_", "_", "_", "_"],
            ["_", "_", "_", "X", "_", "_", "_"],
            ["_", "_", "_", "_", "X", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"]
        ]
        result = dummy_grid.check_winner()
        # Assert
        assert expected == result

    def test_method_returns_o_winner_reverse_diagonal(self):
        # Arrange
        expected = "O"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "O", "_", "_", "_"],
            ["_", "_", "_", "_", "O", "_", "_"],
            ["_", "_", "_", "_", "_", "O", "_"],
            ["_", "_", "_", "_", "_", "_", "O"]
        ]
        result = dummy_grid.check_winner()
        # Assert
        assert expected == result

    def test_method_returns_winner_correctly(self):
        # Arrange
        expected = "X"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "X", "_", "_", "_", "_", "_"],
            ["X", "X", "O", "X", "_", "_", "_"],
            ["_", "X", "_", "O", "_", "_", "X"],
            ["_", "O", "X", "O", "X", "X", "O"],
            ["_", "O", "O", "O", "X", "O", "O"],
            ["X", "O", "_", "X", "_", "_", "O"]
        ]
        result = dummy_grid.check_winner()
        # Assert
        assert expected == result

# @pytest.mark.skip
class TestAvailableSlots:
    def test_method_exists(self):
        # Arrange
        expected = "available_slots"
        # Act
        result = dir(ConnectFourGame)
        # Assert
        assert expected in result

    def test_method_returns_correctly_on_empty_grid(self):
        # Arrange
        expected = "1, 2, 3, 4, 5, 6 or 7"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"]
        ]
        result = dummy_grid.available_slots()
        # Assert
        assert expected == result

    def test_method_returns_correctly_on_full_grid(self):
        # Arrange
        expected = "draw"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["X", "O", "X", "O", "X", "O", "O"],
            ["X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "O"],
            ["O", "X", "O", "X", "O", "X", "X"],
            ["O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "X"]
        ]
        result = dummy_grid.available_slots()
        # Assert
        assert expected == result

    def test_method_returns_correctly_on_with_one_move_left(self):
        # Arrange
        expected = "1"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "O", "X", "O", "X", "O", "O"],
            ["X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "O"],
            ["O", "X", "O", "X", "O", "X", "X"],
            ["O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "X"]
        ]
        result = dummy_grid.available_slots()
        # Assert
        assert expected == result

        # Arrange
        expected = "4"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["X", "O", "X", "_", "X", "O", "O"],
            ["X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "O"],
            ["O", "X", "O", "X", "O", "X", "X"],
            ["O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "X"]
        ]
        result = dummy_grid.available_slots()
        # Assert
        assert expected == result

    def test_method_returns_correctly_on_with_two_moves_left(self):
        # Arrange
        expected = "2 or 3"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["X", "_", "_", "O", "X", "O", "O"],
            ["X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "O"],
            ["O", "X", "O", "X", "O", "X", "X"],
            ["O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "X"]
        ]
        result = dummy_grid.available_slots()
        # Assert
        assert expected == result

        # Arrange
        expected = "5 or 7"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["X", "O", "X", "O", "_", "O", "_"],
            ["X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "O"],
            ["O", "X", "O", "X", "O", "X", "X"],
            ["O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "X"]
        ]
        result = dummy_grid.available_slots()
        # Assert
        assert expected == result

    def test_method_returns_correctly_on_with_some_moves_left(self):
        # Arrange
        expected = "1, 2 or 3"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "_", "_", "O", "X", "O", "O"],
            ["X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "O"],
            ["O", "X", "O", "X", "O", "X", "X"],
            ["O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "X"]
        ]
        result = dummy_grid.available_slots()
        # Assert
        assert expected == result

        # Arrange
        expected = "1, 3, 5 or 7"
        # Act
        dummy_grid = ConnectFourGame()
        dummy_grid._current_board = [
            ["_", "O", "_", "O", "_", "O", "_"],
            ["X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "O"],
            ["O", "X", "O", "X", "O", "X", "X"],
            ["O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "X"]
        ]
        result = dummy_grid.available_slots()
        # Assert
        assert expected == result
        