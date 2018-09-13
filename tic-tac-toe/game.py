"""The tic-tac-toe game class."""
from board import Board
from player import Player


class Game(object):
    """The game class."""

    def __init__(self):
        """Initializer for the game class."""
        self.player_turn = 1
        self.player_one = None
        self.player_two = None
        self._moves = 0
        self.board = None

    def start_game(self):
        """Start the game."""
        self.board = Board()
        self.prompt_players()

    def prompt_players(self):
        """Get player names."""
        print('Player 1, what is your name?')
        name1 = input()
        print('Player 2, what is your name?')
        name2 = input()
        self.create_players(name1, name2)

    def create_players(self, name1, name2):
        """Create a player."""
        if self.player_one is None:
            self.player_one = Player(name1, 'X', 1)
        elif self.player_one and self.player_two is None:
            self.player_two = Player(name2, 'O', 2)
        self.prompt_move()

    def prompt_move(self):
        """Prompt player move."""
        self.board.draw_board()

        if self.player_turn == 1:
            print(self.player_one.name + ' please pick a position.')
            try:
                move = input()
                self.board.place_marker(move, self.player_one.marker)
                self._moves += 1
            except ValueError:
                self.prompt_move()
            if self._moves > 4:
                if self.is_winner(self.board) == '#$':
                    pass
            self.player_turn = 2
            self.prompt_move()
        if self.player_turn == 2:
            print(self.player_two.name + ' please pick a position.')
            try:
                move = input()
                self.board.place_marker(move, self.player_two.marker)
                self._moves += 1
            except ValueError:
                self.prompt_move()
            if self._moves > 4:
                if self.is_winner(self.board) == '#$':
                    pass
            self.player_turn = 1
            self.prompt_move()

    def is_winner(self, board_status):
        """Verify if there is a winner."""
        result = board_status.check_winner()
        if result == 'X':
            print(self.player_one.name + 'WINS!!!!')
            self.start_game()
        elif result == 'O':
            print(self.player_twon.name + 'WINS!!!!')
            self.start_game()
        else:
            return '#$'
