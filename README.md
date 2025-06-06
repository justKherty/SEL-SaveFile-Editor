# SEL-SaveFile-Editor
Python editor of the savefile created by the game Serial Experiments Lain.
Before proceeding, please make yourself knowledgeable of the license used by this Python program. 

-- How it works --

The workflow has been consolidated into a single command-line interface.  The
``cli.py`` script wraps the helper modules and performs every step: converting
the raw save file, marking viewed chapters and writing the final JSON.  Run it
with optional arguments to override the default paths:

```
python cli.py --raw INPUT.txt --chapters CHAPTERS.txt --output OUTPUT.json
```

``CHAPTERS.txt`` should contain a comma-separated list of chapter IDs you have
completed. The script will mark those chapters as ``is_viewed = 1`` in the final
``OUTPUT.json``.
