"""Render Kottakkal is Busy cards to JPEG.

Usage: python3 render.py spec.json OUT_DIR
spec.json example:
{
  "date": "15 നവംബർ 2026",
  "carousel": [ {"label":"TRAFFIC","headline":"...","summary":"...","source":"Manorama","breaking":false}, ... ],
  "single":   {"label":"EVENT","headline":"...","summary":"...","source":"..."},
  "stories":  [ {"label":"ALERT","headline":"...","line":"...","breaking":true}, ... ]
}
Any section may be omitted. Writes cover.jpg, slide-01.jpg.., end.jpg, single.jpg, story-01.jpg..
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import templates as T
from playwright.sync_api import sync_playwright


def main(spec_path, out):
    spec = json.load(open(spec_path, encoding="utf-8"))
    os.makedirs(out, exist_ok=True)
    date = spec["date"]
    jobs = []
    car = spec.get("carousel") or []
    if car:
        jobs.append(("cover.jpg", T.briefing_cover(date, [c["headline"] for c in car]), 1350))
        for i, c in enumerate(car, 1):
            jobs.append((f"slide-{i:02d}.jpg", T.news_card(date, c["label"], c["headline"], c["summary"], c["source"], i, len(car), c.get("breaking", False)), 1350))
        jobs.append(("end.jpg", T.end_slide(date), 1350))
    if spec.get("single"):
        s = spec["single"]
        jobs.append(("single.jpg", T.news_card(date, s["label"], s["headline"], s["summary"], s["source"], breaking=s.get("breaking", False)), 1350))
    for i, s in enumerate(spec.get("stories") or [], 1):
        jobs.append((f"story-{i:02d}.jpg", T.story_card(date, s["label"], s["headline"], s["line"], s.get("breaking", False)), 1920))
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        for name, html, h in jobs:
            pg = b.new_page(viewport={"width": 1080, "height": h})
            pg.set_content(html)
            pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(out, name), type="jpeg", quality=90)
            pg.close()
        b.close()
    print("\n".join(j[0] for j in jobs))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
