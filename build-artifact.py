"""Generate the Artifact-ready copy of the deck.

Claude Artifacts wrap the supplied file in their own
<!doctype html><head>…</head><body> skeleton, so the published file must contain
page content only — no doctype, <html>, <head> or <body> tags of its own.

This strips that wrapper from the source deck and writes artifact.html, which is
gitignored (it is generated, not source). Publish that file with the Artifact
tool; re-running this script and republishing the same path updates the page in
place at the same URL.

    python build-artifact.py
"""

import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
SRC = HERE / "metric-views-in-genie-tcb.html"
OUT = HERE / "artifact.html"

html = SRC.read_text(encoding="utf-8")

style = html[html.index("<style>"): html.index("</style>") + len("</style>")]
content = html[html.index("<body>") + len("<body>"): html.index("</body>")]
body = (style + "\n" + content).strip()

for tag in ("<!doctype", "<html", "<head", "</head", "<body", "</body"):
    if tag in body.lower():
        sys.exit(f"error: {tag}> survived the strip - check the source structure")

OUT.write_text(body + "\n", encoding="utf-8")

slides = len(re.findall(r'<section class="slide', body))
print(f"wrote {OUT.name}  ({len(body):,} bytes, {slides} slides)")
