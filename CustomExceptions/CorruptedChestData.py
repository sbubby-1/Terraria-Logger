class CorruptedChestData(Exception):
    def __init__(self):
        """The Chest data is corrupted."""

        self.message = f"This Chest data is corrupted."
