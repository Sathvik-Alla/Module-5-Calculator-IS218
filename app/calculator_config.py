import os
from dotenv import load_dotenv

load_dotenv()


class CalculatorConfig:
    def __init__(self):
        self.debug = os.getenv("DEBUG", "False") == "True"
        self.history_file = os.getenv("HISTORY_FILE", "history.csv")