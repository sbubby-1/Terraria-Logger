class CorruptedChestData(Exception):
    def __init__(self):
        """An Exception raised for corrupted chest data."""

        self.message = f"This Chest data is corrupted."
