class InvalidDataType(Exception):
    def __init__(self, dataType):
        """An Exception raised for an unrecognized data type."""

        self.message = f"{dataType} is not a recognized data type."
