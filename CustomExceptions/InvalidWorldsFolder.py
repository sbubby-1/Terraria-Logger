class InvalidWorldsFolder(Exception):
    def __init__(self):
        """The Worlds folder filepath is incorrect."""

        self.message = "The Worlds folder filepath is incorrect."
