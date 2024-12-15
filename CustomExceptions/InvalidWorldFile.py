class InvalidWorldFile(Exception):
    def __init__(self, message):
        """An Exception raised when a .wld file of an unsupported version is
        read."""

        self.message = message
