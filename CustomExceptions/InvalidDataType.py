class InvalidDataType(Exception):
    def __init__(self, dataType):
        """The data type is unrecognized."""

        self.message = f"{dataType} is not a recognized data type."
