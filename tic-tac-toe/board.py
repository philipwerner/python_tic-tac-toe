"""The Board class module."""


class Board(object):
    """The board class."""

    def __init__(self):
        """Initializer for the board class."""
        self.current = ['1', '|', '2', '|', '3', '4', '|', '5', '|', '6', '7', '|', '8', '|', '9']

    def place_marker(self, input, marker):
        """Place marker on board."""
        if input == 'quit':
            quit()
        int_input = int(input)
        if int_input > 9 and int_input < 1:
            raise ValueError("Please enter a integer between 1 and 9")
        elif int_input < 10 and int_input > 0:
            for x in range(0, 15):
                if self.current[x] == input:
                    self.current[x] = marker
        else:
            print("Please choose a available position.")
        return self

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
        if check[x] == check[x + 2] and check[x] == check[x + 4]:
            return check[x]
        elif check[x + 5] == check[x + 7] and check[x + 5] == check[x + 9]:
            return check[x + 5]
        elif check[x + 10] == check[x + 12] and check[x + 10] == check[x + 14]:
            return check[x + 10]

        # Check for vertical winner
        elif check[x] == check[x + 5] and check[x] == check[x + 10]:
            return check[x]
        elif check[x + 2] == check[x + 7] and check[x + 2] == check[x + 12]:
            return check[x + 2]
        elif check[x + 4] == check[x + 9] and check[x + 3] == check[x + 14]:
            return check[x + 3]

        # Check for top left to bottom right diagonal win
        elif check[0] == check[7] and check[0] == check[14]:
            return check[0]
        # Check for top right to bottom left diagonal win
        elif check[4] == check[7] and check[4] == check[10]:
            return check[4]
        else:
            return None
