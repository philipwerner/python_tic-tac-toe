"""The Board class module."""


class Board(object):
    """The board class."""

    def __init__(self):
        """Initializer for the board class."""
        self.current = ['1', '|', '2', '|', '3', '4', '|', '5', '|', '6', '7', '|', '8', '|', '9']

    def place_marker(self, input, marker):
        """Place marker on board."""
        try:
            input = int(input)
        except ValueError:
            raise ValueError
        if input > 9 or input < 1:
            raise ValueError("Please enter a integer between 1 and 9")
        for x in range(15):
            if self.current[x] == input:
                self.current[x] = marker
        else:
            raise ValueError("Please choose a available position.")

    def draw_board(self):
        """Display the current board."""
        top = ''
        mid = ''
        btm = ''
        for x in range(5):
            top = top + self.current[x]
        for x in range(5, 10):
            mid = mid + self.current[x]
        for x in range(10, 15):
            btm = btm + self.current[x]
        print(top)
        print(mid)
        print(btm)

    def check_winner(self):
        """Check if there is a winner."""
        check = self.current
        x = 0
        # Check for horizontal winner
        while x < 11:
            if check[x] == check[x + 2] and check[x] == check[x + 4]:
                return check[x]
            elif x < 6:
                x += 5
            else:
                x = 0
        # Check for vertical winner
        while x < 4:
            if check[x] == check[x + 5] and check[x] == check[x + 10]:
                return check[x]
            elif x < 5:
                x += 2
            else:
                x = 0
        # Check for top left to bottom right diagonal win
        if check[0] == check[7] and check[0] == check[14]:
            return check[0]
        # Check for top right to bottom left diagonal win
        elif check[4] == check[7] and check[4] == check[10]:
            return check[4]
        else:
            return None
