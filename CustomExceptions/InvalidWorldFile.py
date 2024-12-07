class InvalidWorldFile(Exception):
    def __init__(self, message):
        """Raised when a .wld file of version <267 is read."""

        self.message = message
