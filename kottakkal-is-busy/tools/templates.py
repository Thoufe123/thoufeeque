"""Premium Kottakkal is Busy card templates (yellow & white).

All cards: FreeSans (has Malayalam), black text, #FFC800 yellow accent.
Sizes: feed/carousel 1080x1350, story 1080x1920.
"""

BASE_CSS = """
*{box-sizing:border-box}
body{margin:0;font-family:'FreeSans',sans-serif;color:#111111}
.stripes{background:repeating-linear-gradient(-45deg,#FFC800 0 34px,#FFFFFF 34px 68px)}
.mast{display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:16px}
.logo{width:54px;height:54px;transform:rotate(45deg);background:#FFC800;border-radius:10px}
.bk{font-weight:bold;font-size:40px;letter-spacing:-1px;line-height:1}
.bb{font-weight:bold;font-size:26px;letter-spacing:4px;line-height:1.15}
.date{font-size:28px;font-weight:bold;color:#111111}
.label{display:inline-block;background:#111111;color:#FFC800;font-weight:bold;font-size:30px;letter-spacing:3px;padding:12px 24px 10px;border-radius:8px}
.label.breaking{background:#FFC800;color:#111111}
.rule{height:6px;background:#FFC800;border-radius:3px}
.foot{background:#FFC800;display:flex;align-items:center;justify-content:space-between;font-weight:bold}
"""


def _page(w, h, body):
    return (f"<!doctype html><html lang='ml'><head><meta charset='utf-8'><style>{BASE_CSS}"
            f".root{{width:{w}px;height:{h}px;background:#FFFFFF;display:flex;flex-direction:column}}"
            f"</style></head><body><div class='root'>{body}</div></body></html>")


def _mast(date, pad="56px 64px 0"):
    return (f"<div class='mast' style='padding:{pad}'>"
            "<div class='brand'><div class='logo'></div><div><div class='bk'>KOTTAKKAL</div>"
            "<div class='bb'>IS BUSY</div></div></div>"
            f"<div class='date'>{date}</div></div>")


def news_card(date, label, headline, summary, source, num=None, total=None, breaking=False):
    """Single news card / carousel slide (1080x1350)."""
    counter = f"<div style='font-size:30px;font-weight:bold;color:#555'>{num:02d} / {total:02d}</div>" if num else ""
    cls = "label breaking" if breaking else "label"
    body = (
        "<div class='stripes' style='height:40px'></div>"
        + _mast(date)
        + "<div style='padding:40px 64px 0'><div class='rule'></div></div>"
        + "<div style='flex-grow:1;padding:0 64px 40px;display:flex;flex-direction:column;justify-content:center;gap:40px'>"
        + f"<div style='display:flex;align-items:center;justify-content:space-between'><span class='{cls}'>{label}</span>{counter}</div>"
        + f"<div style='font-size:80px;font-weight:bold;line-height:1.18'>{headline}</div>"
        + f"<div style='font-size:40px;line-height:1.5;color:#333333'>{summary}</div>"
        + "</div>"
        + f"<div class='foot' style='height:120px;padding:0 64px;font-size:30px'><span>@kottakkal_is_busy</span><span style='font-weight:normal'>Source: {source}</span></div>"
    )
    return _page(1080, 1350, body)


def briefing_cover(date, items):
    """Carousel cover: 'കോട്ടക്കൽ ഇന്ന്' + list of headlines (1080x1350)."""
    rows = "".join(
        f"<div style='display:flex;gap:28px;align-items:flex-start'>"
        f"<div style='flex-shrink:0;width:72px;height:72px;background:#FFC800;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:38px;font-weight:bold'>{i+1:02d}</div>"
        f"<div style='font-size:42px;font-weight:bold;line-height:1.3;padding-top:8px'>{t}</div></div>"
        for i, t in enumerate(items))
    body = (
        "<div class='stripes' style='height:40px'></div>"
        + _mast(date)
        + "<div style='padding:56px 64px 0'><span class='label'>DAILY BRIEFING</span>"
        + "<div style='font-size:120px;font-weight:bold;line-height:1.1;margin-top:28px'>കോട്ടക്കൽ ഇന്ന്</div>"
        + "<div class='rule' style='margin-top:32px'></div></div>"
        + f"<div style='flex-grow:1;padding:48px 64px 0;display:flex;flex-direction:column;gap:34px'>{rows}</div>"
        + "<div class='foot' style='height:120px;padding:0 64px;font-size:32px'><span>Swipe ചെയ്യൂ →</span><span>@kottakkal_is_busy</span></div>"
    )
    return _page(1080, 1350, body)


def end_slide(date):
    body = (
        "<div class='stripes' style='height:40px'></div>"
        + _mast(date)
        + "<div style='flex-grow:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;padding:0 80px;text-align:center'>"
        + "<div style='width:300px;height:300px;transform:rotate(45deg);background:#FFC800;border-radius:44px;display:flex;align-items:center;justify-content:center'>"
        + "<div style='transform:rotate(-45deg);font-size:150px;font-weight:bold'>!</div></div>"
        + "<div style='font-size:70px;font-weight:bold;line-height:1.2;margin-top:40px'>നിങ്ങളുടെ നാട്ടിലെ news അയക്കൂ</div>"
        + "<div style='font-size:40px;color:#333'>DM ചെയ്യൂ • Follow ചെയ്യൂ • Share ചെയ്യൂ</div></div>"
        + "<div class='foot' style='height:120px;padding:0 64px;font-size:32px;justify-content:center'>@kottakkal_is_busy</div>"
    )
    return _page(1080, 1350, body)


def story_card(date, label, headline, line, breaking=False):
    """Story card for quick updates (1080x1920)."""
    cls = "label breaking" if breaking else "label"
    body = (
        "<div class='stripes' style='height:64px'></div>"
        + _mast(date, pad="160px 80px 0")
        + "<div style='flex-grow:1;display:flex;flex-direction:column;justify-content:center;gap:44px;padding:0 80px'>"
        + f"<div><span class='{cls}' style='font-size:38px'>{label}</span></div>"
        + f"<div style='font-size:100px;font-weight:bold;line-height:1.16'>{headline}</div>"
        + f"<div style='font-size:48px;line-height:1.45;color:#333'>{line}</div></div>"
        + "<div class='foot' style='height:260px;padding:0 80px 80px;font-size:40px;justify-content:center'>@kottakkal_is_busy</div>"
    )
    return _page(1080, 1920, body)
