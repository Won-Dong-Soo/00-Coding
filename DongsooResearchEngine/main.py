from pathlib import Path

from core.database import DatabaseManager

def initialize():

    Path("data").mkdir(exist_ok=True)
    Path("data/cache").mkdir(exist_ok=True)

    db = DatabaseManager()
    db.initialize()

    print("Dongsoo Research Engine Initialized")

if __name__ == "__main__":
    initialize()