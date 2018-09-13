"""Player class module."""


class Player(object):
    """The player class."""

    def __init__(self, name, marker=None, position=None):
        """Initializer for the player class."""
        self.name = name
        self.marker = None
        self.number = None
        self.position = None
        if name is None:
            raise ValueError("Must enter a valid name.")
