"""The tic-tac-toe game class."""
from board import Board
from player import Player


class Game(object):
    """The game class."""

    def __init__(self):
        """Initializer for the game class."""
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
        print('Welcome to Tic-Tac-Toe!')
        print('Player 1, what is your name?')
        name1 = input()
        print('Player 2, what is your name?')
        name2 = input()
        self.create_players(name1, name2)

    def create_players(self, name1, name2):
        """Create a player."""
        self.player_one = Player(name1, 'X', 1)
        self.player_two = Player(name2, 'O', 2)
        self.prompt_player_one()

    def prompt_player_one(self):
        """Prompt player one."""
        self.board.draw_board()
        print(self.player_one.name + ' please pick a position.')
        move = input()
        self.board.place_marker(move, 'X')
        self._moves += 1
        if self._moves > 4:
            if self.is_winner(self.board) == '#$':
                self.prompt_player_two()
        else:
            self.prompt_player_two()

    def prompt_player_two(self):
        """Prompt player two."""
        self.board.draw_board()
        print(self.player_two.name + ' please pick a position.')
        try:
            move = input()
            self.board.place_marker(move, 'O')
            self._moves += 1
            if self._moves > 4:
                if self.is_winner(self.board) == '#$':
                    self.prompt_player_one()
        except ValueError:
            self.prompt_player_two()
        self.prompt_player_one()

    def is_winner(self, board_status):
        """Verify if there is a winner."""
        result = board_status.check_winner()
        if result == 'X':
            self.player_one.wins += 1
            print(self.player_one.name + ' WINS!!!!')
            self.play_again()
        elif result == 'O':
            self.player_two.wins += 1
            print(self.player_twon.name + ' WINS!!!!')
            self.play_again()
        elif self._moves == 9:
            print('It is a draw.')
            self.play_again()
        else:
            return '#$'

    def play_again(self):
        """Check if another game is to be played."""
        print('Would you like to play again?(y/n or yes/no)')
        reply = input().lower()
        if reply == 'y' or reply == 'yes':
            self._moves = 0
            self.start_game()
        elif reply == 'n' or reply == 'no':
            quit()
        else:
            print('Please enter y/n or yes/no')
            self.play_again()

    def same_players(self):
        """Check if same players are playing."""
        print('Is player one still ' + self.player_one.name + '?')
        reply = input().lower()
        if reply == 'y' or reply == 'yes':
            print('Is player two still ' + self.player_two.name + '?')
            reply_two = input().lower()
            if reply_two == 'y' or reply_two == 'yes':
                print(self.player_one.name + ' has ' + self.player_one.wins + ' wins.')
                print(self.player_two.name + ' has ' + self.player_two.wins + ' wins.')
                self.prompt_player_one()
            elif reply_two == 'n' or reply_two == 'no':
                print("Enter a name for player two.")
                new_name = input()
                self.player_two = Player(new_name, 'O', 2)
                self.prompt_player_one()
        elif reply == 'n' or reply == 'no':
                print("Enter a name for player one.")
                new_name = input()
                self.player_one = Player(new_name, 'X', 1)
                print('Welcome ' + self.player_one.name + ', is player two the same player?')
                reply_two = input()
                if reply_two == 'y' or reply_two == 'yes':
                    print(self.player_one.name + ' has ' + self.player_one.wins + ' wins.')
                    print(self.player_two.name + ' has ' + self.player_two.wins + ' wins.')
                    self.prompt_player_one()
                elif reply_two == 'n' or reply_two == 'no':
                    print("Enter a name for player two.")
                    new_name = input()
                    self.player_two = Player(new_name, 'O', 2)
                    self.prompt_player_one()
        else:
            print('Thank you for playing.')
            exit()
