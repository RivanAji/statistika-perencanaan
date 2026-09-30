"""Check local links and downloadable assets in a GitHub Pages style build."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit


ROOT = Path(__file__).resolve().parents[1] / "dist"
BASE = "/statistik-perencanaan-pwk/"
ORIGIN = "https://example.github.io"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            value = dict(attrs).get("href")
            if value:
                self.hrefs.append(value)


failures = []
count = 0
for source in ROOT.rglob("*.html"):
    if source.name == "404.html":
        continue
    relative = source.relative_to(ROOT)
    route = "/" if relative == Path("index.html") else "/" + str(relative.parent) + "/"
    current = ORIGIN + BASE.rstrip("/") + route
    parser = Links()
    parser.feed(source.read_text(encoding="utf-8"))
    for href in parser.hrefs:
        resolved = urlsplit(urljoin(current, href))
        if resolved.netloc != "example.github.io":
            continue
        if not resolved.path.startswith(BASE):
            failures.append(f"{relative}: outside base: {href}")
            continue
        target_route = resolved.path[len(BASE):]
        target = ROOT / target_route
        if resolved.path.endswith("/"):
            target /= "index.html"
        elif target.is_dir():
            target /= "index.html"
        if not target.is_file():
            failures.append(f"{relative}: missing: {href} -> {target_route}")
        count += 1

for failure in failures:
    print(failure)
print(f"Checked {count} local links; {len(failures)} failures.")
raise SystemExit(1 if failures else 0)
