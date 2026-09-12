from pathlib import Path

def parse_text(file_path):

    return Path(
        file_path
    ).read_text(
        encoding="utf-8",
        errors="ignore"
    )