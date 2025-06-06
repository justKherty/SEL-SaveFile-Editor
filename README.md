# SEL-SaveFile-Editor
Python editor of the savefile created by the game Serial Experiments Lain.
Before proceeding, please make yourself knowledgeable of the license used by this Python program. 

-- How it works --

The workflow has been consolidated into a single entry point, ``SSFE.py``.  It
converts the raw save file, applies chapter updates from ``CHAPTERS.txt`` and
writes the final JSON.  Run the script with optional arguments to override the
default paths:

```
python SSFE.py --raw INPUT.txt --chapters CHAPTERS.txt --output OUTPUT.json
```

``CHAPTERS.txt`` should contain a comma-separated list of chapter IDs you have
completed. The script will mark those chapters as ``is_viewed = 1`` in the final
``OUTPUT.json``.
