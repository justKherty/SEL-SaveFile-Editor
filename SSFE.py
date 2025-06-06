"""Utility script to orchestrate save file conversions."""

from argparse import ArgumentParser

from SSFE_JSON_Convert import convert_raw_to_json
from SSFE_main import (
    load_chapters,
    mark_chapters_viewed,
    save_json,
)


def process_save_file(raw_save: str, chapters_path: str, output: str) -> None:
    """Convert ``raw_save`` and mark chapters listed in ``chapters_path``."""

    data = convert_raw_to_json(raw_save)
    chapters = load_chapters(chapters_path)
    mark_chapters_viewed(data, chapters)
    save_json(output, data)


def main() -> None:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--raw", default="INPUT.txt", help="Raw save file")
    parser.add_argument(
        "--chapters", default="CHAPTERS.txt", help="Chapter list to mark"
    )
    parser.add_argument("--output", default="OUTPUT.json", help="Final JSON file")
    args = parser.parse_args()

    process_save_file(args.raw, args.chapters, args.output)


if __name__ == "__main__":
    main()
