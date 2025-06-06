"""Utility script to orchestrate save file conversions."""

from SSFE_JSON_Convert import convert_raw_to_json
from SSFE_main import (
    load_chapters,
    mark_chapters_viewed,
    save_json,
)


def main() -> None:
    data = convert_raw_to_json()
    chapters = load_chapters("CHAPTERS.txt")
    mark_chapters_viewed(data, chapters)
    save_json("OUTPUT.json", data)


if __name__ == "__main__":
    main()
