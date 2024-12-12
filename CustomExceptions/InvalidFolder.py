class InvalidFolder(Exception):
    def __init__(self, folderName):
        """The Worlds folder filepath is incorrect."""

        self.message = f"The {folderName} folder filepath is incorrect."
