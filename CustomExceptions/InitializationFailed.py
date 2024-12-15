class InitializationFailed(Exception):
    def __init__(self):
        """Exception raised when initialization was done incorrectly or did not
        finish."""

        self.message = f"Initialization was done incorrectly or did not finish."
