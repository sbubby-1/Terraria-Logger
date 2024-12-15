class InvalidFolder(Exception):
    def __init__(self, folderName):
        """An Exception raised in the case of an invalid folder filepath."""

        self.message = f"The {folderName} folder filepath is incorrect."
