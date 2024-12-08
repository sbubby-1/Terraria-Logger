class InitializationFailed(Exception):
    def __init__(self):
        """Initialization was done incorrectly or did not finish."""

        self.message = f"Initialization was done incorrectly or did not finish."
