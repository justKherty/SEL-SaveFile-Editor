"""Command-line interface for save file editing."""

from argparse import ArgumentParser

from SSFE import process_save_file


def main() -> None:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--raw", default="INPUT.txt", help="Raw save file")
    parser.add_argument("--chapters", default="CHAPTERS.txt", help="Chapter list to mark")
    parser.add_argument("--output", default="OUTPUT.json", help="Final JSON file")
    args = parser.parse_args()

    process_save_file(args.raw, args.chapters, args.output)


if __name__ == "__main__":
    main()
