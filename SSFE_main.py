"""Update chapter completion states based on a user provided file."""

import json
from pathlib import Path

INPUT_FILE = "INPUT.json"
OUTPUT_FILE = "OUTPUT.json"
CHAPTERS_FILE = "CHAPTERS.txt"


def load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def save_json(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def load_chapters(path: str) -> list[str]:
    if not Path(path).exists():
        return []
    with open(path, "r") as f:
        text = f.read().replace("\n", "").replace(" ", "")
    return [c for c in text.split(",") if c]


def main() -> None:
    data = load_json(INPUT_FILE)
    chapters = load_chapters(CHAPTERS_FILE)
    for chapter in chapters:
        if chapter in data:
            data[chapter]["is_viewed"] = 1
    save_json(OUTPUT_FILE, data)


if __name__ == "__main__":
    main()
