"""Generate the profile README graphics (self-hosted SVG, no third-party widgets).

Run:  python tools/make_assets.py
Edit the CONFIG block, re-run, commit the files in assets/. Pure standard library.
"""
from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

# ----------------------------------------------------------------------------- CONFIG
NAME = "Himanshu Upadhyay"
HEADLINE = "Automotive Data Engineer"
SUBLINE = "Azure  ·  PySpark  ·  Delta Lake  ·  SQL  ·  MATLAB/Simulink"
TAGLINE = "I build data pipelines you can trust, and prove it with tests."
LINKEDIN_TEXT = "LinkedIn  /in/hup2000"
EMAIL_TEXT = "himan.upde@gmail.com"

# (category, [(label, core)]) core=True -> solid chip, False -> dashed chip (included as template / design)
STACK = [
    ("Languages", [("Python", True), ("SQL", True), ("PySpark", True), ("Spark SQL", True), ("MATLAB / Simulink", True)]),
    ("Azure and lakehouse", [("ADLS Gen2", True), ("Azure Databricks", True), ("Azure Data Factory", True), ("Delta Lake", True),
                             ("Event Hubs", False), ("Synapse", False), ("Key Vault", False)]),
    ("Data engineering", [("ETL / ELT", True), ("Data modelling", True), ("Star schema", True), ("Medallion architecture", True),
                          ("Data quality", True), ("Incremental loads", True)]),
    ("Engineering practice", [("pytest", True), ("GitHub Actions", True), ("Git", True), ("Azure DevOps", False), ("Power BI", False)]),
]
# ------------------------------------------------------------------------------------

BG, CARD, BORDER, TEXT, MUTED = "#0d1117", "#161b22", "#30363d", "#e6edf3", "#8b949e"
BLUE, BRONZE, SILVER, GOLD, GREEN = "#58a6ff", "#cd7f32", "#c0c7d0", "#e3b341", "#3fb950"
FONT = "Segoe UI, -apple-system, Helvetica, Arial, sans-serif"
OUT = Path(__file__).resolve().parents[1] / "assets"


def svg(w: int, h: int, body: str, title: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">'
            f'<title>{escape(title)}</title>{body}</svg>')


def banner() -> str:
    b = [
        '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset="1" stop-color="#101c33"/></linearGradient></defs>',
        f'<rect x="1" y="1" width="998" height="258" rx="14" fill="url(#g)" stroke="{BORDER}"/>',
        f'<text x="48" y="104" font-family="{FONT}" font-size="46" font-weight="700" fill="{TEXT}">{escape(NAME)}</text>',
        f'<text x="48" y="146" font-family="{FONT}" font-size="26" font-weight="600" fill="{BLUE}">{escape(HEADLINE)}</text>',
        f'<text x="48" y="184" font-family="{FONT}" font-size="17" fill="{MUTED}" xml:space="preserve">{escape(SUBLINE)}</text>',
        f'<text x="48" y="222" font-family="{FONT}" font-size="16" fill="{TEXT}">{escape(TAGLINE)}</text>',
    ]
    # medallion motif: three stacked layers with flow arrows
    layers = [("BRONZE", "raw, as received", BRONZE), ("SILVER", "validated, deduplicated", SILVER), ("GOLD", "analytics-ready", GOLD)]
    for i, (name, sub, col) in enumerate(layers):
        y = 38 + i * 72
        b += [
            f'<rect x="650" y="{y}" width="302" height="54" rx="10" fill="{CARD}" stroke="{col}" stroke-width="1.6"/>',
            f'<rect x="650" y="{y}" width="8" height="54" rx="4" fill="{col}"/>',
            f'<text x="676" y="{y+24}" font-family="{FONT}" font-size="16" font-weight="700" fill="{col}" letter-spacing="1.5">{name}</text>',
            f'<text x="676" y="{y+43}" font-family="{FONT}" font-size="13" fill="{MUTED}">{escape(sub)}</text>',
        ]
        if i < 2:
            b.append(f'<path d="M801 {y+56} v14 m-5 -6 l5 6 l5 -6" fill="none" stroke="{MUTED}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>')
    return svg(1000, 260, "".join(b), f"{NAME}, {HEADLINE}")


def stack() -> str:
    label_w, x0, max_x, chip_h, gap, row_gap = 196, 24, 976, 32, 10, 14
    body, y = [], 24
    for cat, items in STACK:
        cx, cy = x0 + label_w, y
        body.append(f'<text x="{x0}" y="{y+21}" font-family="{FONT}" font-size="14" font-weight="600" fill="{MUTED}">{escape(cat)}</text>')
        for label, core in items:
            w = int(len(label) * 7.7 + 30)
            if cx + w > max_x:
                cx, cy = x0 + label_w, cy + chip_h + 10
            if core:
                body.append(f'<rect x="{cx}" y="{cy}" width="{w}" height="{chip_h}" rx="16" fill="#12263f" stroke="{BLUE}" stroke-width="1.2"/>')
                col = TEXT
            else:
                body.append(f'<rect x="{cx}" y="{cy}" width="{w}" height="{chip_h}" rx="16" fill="none" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="4 3"/>')
                col = MUTED
            body.append(f'<text x="{cx + w/2}" y="{cy+21}" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{col}">{escape(label)}</text>')
            cx += w + gap
        y = cy + chip_h + row_gap
        body.append(f'<line x1="{x0}" y1="{y-7}" x2="{max_x}" y2="{y-7}" stroke="{BORDER}" stroke-width="1"/>')
    y += 4
    body += [
        f'<rect x="{x0}" y="{y}" width="26" height="14" rx="7" fill="#12263f" stroke="{BLUE}"/>',
        f'<text x="{x0+36}" y="{y+12}" font-family="{FONT}" font-size="13" fill="{MUTED}">core tools I work with</text>',
        f'<rect x="{x0+230}" y="{y}" width="26" height="14" rx="7" fill="none" stroke="{MUTED}" stroke-dasharray="4 3"/>',
        f'<text x="{x0+266}" y="{y+12}" font-family="{FONT}" font-size="13" fill="{MUTED}">appear in my projects as documented templates or designs (not deployed)</text>',
    ]
    h = y + 36
    inner = f'<rect x="1" y="1" width="998" height="{h-2}" rx="14" fill="{BG}" stroke="{BORDER}"/>' + "".join(body)
    return svg(1000, h, inner, "Technology stack")


def button(text: str, color: str, icon: str) -> str:
    w = int(len(text) * 9.4 + 70)
    body = (f'<rect x="1" y="1" width="{w-2}" height="40" rx="20" fill="{CARD}" stroke="{color}" stroke-width="1.4"/>'
            f'<g transform="translate(18 11)" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{icon}</g>'
            f'<text x="46" y="26" font-family="{FONT}" font-size="15" font-weight="600" fill="{TEXT}">{escape(text)}</text>')
    return svg(w, 42, body, text)


LINK_ICON = '<path d="M7 11a4 4 0 0 0 5.7 0l2.6-2.6a4 4 0 0 0-5.7-5.7L8.5 3.8"/><path d="M11 7a4 4 0 0 0-5.7 0L2.7 9.6a4 4 0 0 0 5.7 5.7l1.1-1.1"/>'
MAIL_ICON = '<rect x="1" y="3" width="16" height="12" rx="2"/><path d="M2 5l7 5 7-5"/>'


def main() -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / "banner.svg").write_text(banner(), encoding="utf-8")
    (OUT / "stack.svg").write_text(stack(), encoding="utf-8")
    (OUT / "btn-linkedin.svg").write_text(button(LINKEDIN_TEXT, BLUE, LINK_ICON), encoding="utf-8")
    (OUT / "btn-email.svg").write_text(button(EMAIL_TEXT, GREEN, MAIL_ICON), encoding="utf-8")
    print("wrote", sorted(p.name for p in OUT.glob("*.svg")))


if __name__ == "__main__":
    main()
