#!/usr/bin/env python3
"""Re-issues the drawing set on github.com/tushar-cr7.

Reads REVORA's commit history (GitHub REST API) and solve stats (LeetCode's
public GraphQL endpoint), then redraws every sheet twice: blueprint for
GitHub's dark theme, whiteprint for light. Standard library only.
If a source is unreachable, the last verified data is kept - never guessed.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import textwrap
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "drawings"
STATE = ROOT / "data" / "state.json"
GH_USER, LC_USER, PRODUCT = "tushar-cr7", "Tusharr_07", "REVORA"

MONO = "ui-monospace,SFMono-Regular,'SF Mono','Cascadia Mono',Consolas,'Liberation Mono',Menlo,monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"


class Ink(dict):
    __getattr__ = dict.__getitem__


INKS = {
    "dark": Ink(bg="#0A1526", grid="#0F2039", grid2="#152A4B", ink="#DCE7FF", dim="#8DA1C6",
                faint="#34507E", hatch="#2E4A7A", amber="#F5A623", coral="#FF5A60",
                green="#27C48C", violet="#A083FF", indigo="#8199FF"),
    "light": Ink(bg="#F7F5EF", grid="#EDE9DF", grid2="#E0D9C9", ink="#172238", dim="#55637C",
                 faint="#B7BFCD", hatch="#A5AFC2", amber="#B86A04", coral="#CF333B",
                 green="#08845C", violet="#6A43D6", indigo="#3450CF"),
}


# ── data ────────────────────────────────────────────────────────────────────

def http(url: str, data: bytes | None = None, headers: dict | None = None):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "tushar-cr7-drawing-set", **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read(), r.headers


def fetch_revora() -> dict:
    headers = {"Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    body, h = http(f"https://api.github.com/repos/{GH_USER}/{PRODUCT}/commits?per_page=1", headers=headers)
    latest = json.loads(body)[0]
    last_page = re.search(r'[?&]page=(\d+)>; rel="last"', h.get("Link") or "")
    return {
        "commits": int(last_page.group(1)) if last_page else 1,
        "sha": latest["sha"][:7],
        "message": latest["commit"]["message"].splitlines()[0],
        "date": latest["commit"]["committer"]["date"][:10],
    }


def fetch_leetcode() -> dict:
    year = dt.date.today().year
    query = """query($u:String!,$y:Int,$p:Int){matchedUser(username:$u){
      submitStatsGlobal{acSubmissionNum{difficulty count}}
      languageProblemCount{languageName problemsSolved}
      cur:userCalendar(year:$y){streak totalActiveDays submissionCalendar}
      prev:userCalendar(year:$p){submissionCalendar}}}"""
    payload = json.dumps({"query": query, "variables": {"u": LC_USER, "y": year, "p": year - 1}}).encode()
    body, _ = http("https://leetcode.com/graphql", payload,
                   {"Content-Type": "application/json", "Referer": f"https://leetcode.com/u/{LC_USER}/"})
    u = json.loads(body)["data"]["matchedUser"]
    solved = {x["difficulty"].lower(): x["count"] for x in u["submitStatsGlobal"]["acSubmissionNum"]}
    calendar: dict[str, int] = {}
    for part in (u["prev"], u["cur"]):
        for ts, n in json.loads(part["submissionCalendar"] or "{}").items():
            calendar[dt.datetime.fromtimestamp(int(ts), dt.timezone.utc).date().isoformat()] = n
    langs = sorted(((x["languageName"], x["problemsSolved"]) for x in u["languageProblemCount"]), key=lambda x: -x[1])
    return {
        "total": solved["all"], "easy": solved["easy"], "medium": solved["medium"], "hard": solved["hard"],
        "year": year, "active_days": u["cur"]["totalActiveDays"], "max_streak": u["cur"]["streak"],
        "languages": langs, "calendar": dict(sorted(calendar.items())),
    }


# ── svg primitives ──────────────────────────────────────────────────────────

def num(v) -> str:
    if isinstance(v, float):
        s = f"{v:.2f}".rstrip("0").rstrip(".")
        return "0" if s == "-0" else s
    return str(v)


def el(tag: str, body: str | None = None, **kw) -> str:
    attrs = " ".join(f'{k.rstrip("_").replace("_", "-")}="{num(v)}"' for k, v in kw.items() if v is not None)
    return f"<{tag} {attrs}/>" if body is None else f"<{tag} {attrs}>{body}</{tag}>"


def T(x, y, s, fill, size=11, anchor=None, weight=None, ls=None, sans=False, opacity=None, cls=None):
    return el("text", escape(str(s)), x=x, y=y, fill=fill, font_size=size, text_anchor=anchor, font_weight=weight,
              letter_spacing=ls, opacity=opacity, class_=("s" if sans else "m") + (f" {cls}" if cls else ""))


def L(x1, y1, x2, y2, stroke, w=1, dash=None, opacity=None):
    return el("line", x1=x1, y1=y1, x2=x2, y2=y2, stroke=stroke, stroke_width=w, stroke_dasharray=dash, opacity=opacity)


def R(x, y, w, h, fill="none", stroke=None, sw=None, rx=None, dash=None, opacity=None):
    return el("rect", x=x, y=y, width=w, height=h, fill=fill, stroke=stroke, stroke_width=sw, rx=rx,
              stroke_dasharray=dash, opacity=opacity)


def P(d, stroke=None, w=1, fill="none", dash=None, opacity=None):
    return el("path", d=d, stroke=stroke, stroke_width=w, fill=fill, stroke_dasharray=dash, opacity=opacity)


def C(cx, cy, r, fill="none", stroke=None, sw=None, cls=None):
    return el("circle", cx=cx, cy=cy, r=r, fill=fill, stroke=stroke, stroke_width=sw, class_=cls)


def defs(k: Ink) -> str:
    return f"""<defs>
<pattern id="g1" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="{k.grid}"/></pattern>
<pattern id="g2" width="100" height="100" patternUnits="userSpaceOnUse"><rect width="100" height="100" fill="url(#g1)"/><path d="M100 0H0V100" fill="none" stroke="{k.grid2}"/></pattern>
<pattern id="wip" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><line y2="8" stroke="{k.amber}" stroke-width="1.2" opacity=".35"/></pattern>
<pattern id="earth" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><line y2="9" stroke="{k.faint}" stroke-width=".8"/></pattern>
<pattern id="concrete" width="18" height="18" patternUnits="userSpaceOnUse"><g fill="{k.hatch}"><circle cx="3" cy="4" r="1.1"/><circle cx="12" cy="11" r=".8"/><circle cx="15" cy="3" r=".6"/><circle cx="6" cy="15" r=".7"/></g><g fill="none" stroke="{k.hatch}" stroke-width=".8"><path d="M9 3l2.2 3.6H6.8z"/><path d="M2 9.5l2 3.2H0z"/><path d="M13 14l2 3.2h-4z"/></g></pattern>
<filter id="stampink"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="7" result="n"/><feColorMatrix in="n" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -4 3.2" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in"/></filter>
</defs>"""


def frame(w: int, h: int, k: Ink) -> str:
    m = 16
    out = [R(0, 0, w, h, fill=k.bg, rx=12), R(0, 0, w, h, fill="url(#g2)", rx=12, opacity=.75),
           R(m, m, w - 2 * m, h - 2 * m, stroke=k.ink, sw=1.3, opacity=.8)]
    cw = (w - 2 * m) / 8
    for i in range(8):
        cx = m + cw * (i + .5)
        out += [T(cx, 11.5, i + 1, k.dim, 8, "middle"), T(cx, h - 4.5, i + 1, k.dim, 8, "middle")]
        if i:
            x = m + cw * i
            out += [L(x, m, x, m - 5, k.dim, .7), L(x, h - m, x, h - m + 5, k.dim, .7)]
    rows = max(3, round((h - 2 * m) / 150))
    rh = (h - 2 * m) / rows
    for j in range(rows):
        cy = m + rh * (j + .5) + 3
        out += [T(8, cy, "ABCDEFGH"[j], k.dim, 8, "middle"), T(w - 8, cy, "ABCDEFGH"[j], k.dim, 8, "middle")]
        if j:
            y = m + rh * j
            out += [L(m, y, m - 5, y, k.dim, .7), L(w - m, y, w - m + 5, y, k.dim, .7)]
    return "".join(out)


def svg(w: int, h: int, k: Ink, title: str, body: str, css: str = "", framed: bool = True) -> str:
    style = f"<style>.m{{font-family:{MONO}}}.s{{font-family:{SANS}}}{css}</style>"
    label = escape(title, {'"': "&quot;"})
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{label}"><title>{label}</title>{style}{defs(k)}'
            f'{frame(w, h, k) if framed else ""}{body}</svg>\n')


def topbar(w, k, left):
    return T(36, 42, left, k.dim, 9.5, ls=1.6) + T(w - 36, 42, "SCALE: NTS", k.dim, 9.5, "end", ls=1.6) + \
        L(36, 52, w - 36, 52, k.faint, .8)


def cell(label, value, width=None, color=None, size=12):
    return label, value, width, color, size


def title_block(x, y, w, h, cells, k):
    out = [R(x, y, w, h, fill=k.bg, stroke=k.ink, sw=1.2)]
    fixed = sum(c[2] for c in cells if c[2])
    cx = x
    for i, (label, value, cw, color, size) in enumerate(cells):
        cw = cw or (w - fixed)
        if i:
            out.append(L(cx, y, cx, y + h, k.ink, .8))
        out += [T(cx + 8, y + 12.5, label, k.dim, 7.5, ls=1.3),
                T(cx + 8, y + h - 10, value, color or k.ink, size, weight=700)]
        cx += cw
    return "".join(out)


def stamp(cx, cy, w, h, line1, line2, color, rot):
    return (f'<g transform="translate({num(cx)} {num(cy)}) rotate({num(rot)})" filter="url(#stampink)" opacity=".95">'
            + R(-w / 2, -h / 2, w, h, stroke=color, sw=2.2, rx=3)
            + R(-w / 2 + 4, -h / 2 + 4, w - 8, h - 8, stroke=color, sw=.8, rx=2)
            + T(0, -1, line1, color, 15, "middle", 800, 2)
            + T(0, 15, line2, color, 9.5, "middle", 700, 1.5) + "</g>")


def bubble(cx, cy, top, bottom, k, color=None):
    c = color or k.ink
    return (C(cx, cy, 15, fill=k.bg, stroke=c, sw=1.2) + L(cx - 15, cy, cx + 15, cy, c, .8)
            + T(cx, cy - 4, top, c, 9, "middle", 700) + T(cx, cy + 10.5, bottom, c, 7.5, "middle", 700))


def crane(k, mx, ground, top, jl, jr, hook_x, hook_y):
    x0, x1 = mx - 5, mx + 5
    out = [L(x0, ground, x0, top, k.ink, 1.1), L(x1, ground, x1, top, k.ink, 1.1)]
    zig, y, flip = [], ground, False
    while y - 12 >= top:
        zig.append(f"M{x1 if flip else x0} {y}L{x0 if flip else x1} {y - 12}")
        y, flip = y - 12, not flip
    out.append(P("".join(zig), k.ink, .6))
    jb = top + 8
    out += [L(jl, top, jr, top, k.ink, 1.1), L(jl, jb, jr, jb, k.ink, 1.1), L(jl, top, jl, jb, k.ink, 1.1)]
    zig, x, up = [], jl, True
    while x + 12 <= jr:
        zig.append(f"M{x} {jb if up else top}L{x + 12} {top if up else jb}")
        x, up = x + 12, not up
    out.append(P("".join(zig), k.ink, .6))
    ax, ay = mx, top - 24
    out += [P(f"M{x0} {top}L{ax} {ay}L{x1} {top}", k.ink, 1),
            L(ax, ay, jl + 24, top, k.ink, .6), L(ax, ay, jr - 4, top, k.ink, .6),
            R(jr - 24, jb, 20, 15, fill=k.ink, opacity=.85),
            R(x1 + 1, jb + 1, 14, 11, fill=k.bg, stroke=k.ink, sw=.9),
            R(mx - 13, ground - 1, 26, 6, fill=k.ink),
            R(hook_x - 6, jb, 12, 4, fill=k.ink),
            L(hook_x, jb + 4, hook_x, hook_y, k.ink, .7),
            P(f"M{hook_x} {hook_y}v4a4 4 0 1 1 -6 3.5", k.ink, 1.3),
            C(ax, ay - 3, 3.2, fill=k.coral, cls="beacon")]
    return "".join(out)


def scaffold(k, x, y, w, h):
    out = [L(px, y - 10, px, y + h, k.amber, 1) for px in (x - 14, x - 6, x + w + 6, x + w + 14)]
    lv = y - 4
    while lv + 14 <= y + h:
        out += [L(x - 14, lv, x - 6, lv, k.amber, 1), L(x + w + 6, lv, x + w + 14, lv, k.amber, 1),
                L(x - 14, lv, x - 6, lv + 14, k.amber, .6), L(x + w + 6, lv + 14, x + w + 14, lv, k.amber, .6)]
        lv += 14
    return "".join(out)


def tag(k, x, y, n):
    return (R(x, y - 9, 36, 18, fill=k.bg, stroke=k.green, sw=1, rx=9)
            + P(f"M{x + 8} {y}l3 3 6-6", k.green, 1.6) + T(x + 29, y + 3.5, n, k.green, 10, "end", 700))


def arrow(x, y, k, color=None, direction="right"):
    c = color or k.ink
    d = {"right": f"M{x} {y}l-6 -3.5v7z", "down": f"M{x} {y}l-3.5 -6h7z", "left": f"M{x} {y}l6 -3.5v7z"}[direction]
    return P(d, fill=c)


BEACON = ".beacon{animation:beacon 2.4s steps(1,end) infinite}@keyframes beacon{50%{opacity:.12}}" \
         "@media (prefers-reduced-motion:reduce){.beacon{animation:none}}"


# ── sheets ──────────────────────────────────────────────────────────────────

def cover(k: Ink, s: dict) -> str:
    W, H = 880, 600
    rv, lc = s["revora"], s["leetcode"]
    rev = f'{rv["commits"]:02d}'
    b = [topbar(W, k, "DRAWING SET TJ  ·  SHEET G-001  ·  COVER"),
         T(40, 134, "TUSHAR", k.ink, 76, weight=800, ls=-1, sans=True),
         T(40, 208, "JOSHI", k.ink, 76, weight=800, ls=-1, sans=True),
         R(44, 228, 10, 10, fill=k.amber),
         T(62, 237.5, "ENGINEER — UNDER CONSTRUCTION", k.amber, 13, weight=700, ls=2.4),
         T(44, 272, "B.TECH CSE · SRM INSTITUTE OF SCIENCE", k.ink, 12),
         T(44, 291, "AND TECHNOLOGY · CLASS OF 2028 · CHENNAI", k.ink, 12),
         L(44, 314, 470, 314, k.faint),
         T(44, 340, "CURRENTLY ON SITE", k.dim, 9.5, ls=2),
         T(42, 380, "REVORA", k.indigo, 36, weight=800, ls=5, sans=True),
         T(44, 404, "revenue recovery infrastructure", k.ink, 12.5),
         T(44, 423, "AI proposes · deterministic rules decide", k.dim, 12.5),
         stamp(196, 470, 300, 52, "ISSUED FOR CONSTRUCTION", f"REV {rev} · {rv['date']}", k.amber, -3.5)]

    g, x0, x1, fh = 430, 600, 760, 26
    b += [T(530, 84, "KEY PLAN", k.dim, 9.5, ls=2), T(530, 98, "the whole set, one glance", k.dim, 9),
          R(548, g, 292, 60, fill="url(#earth)")]
    counts = [lc["easy"], lc["medium"], lc["hard"]]
    shown = [round(24 * c / max(1, sum(counts))) for c in counts]
    px = x0 + 6
    for depth, n in zip((22, 38, 56), shown):
        for _ in range(n):
            b.append(R(px, g, 2, depth, fill=k.ink, opacity=.85))
            px += 6.2
    b.append(L(520, g, 840, g, k.ink, 1.8))
    floors = [("CAMPUS-APEX", "2025"), ("DSA-IN-CPP", "2025"), ("A* VISUALIZER", "2026"),
              ("3D-SHEARING", "2026"), ("DAILYFLOW", "2026")]
    for i, (name, year) in enumerate(floors):
        y = g - (i + 1) * fh
        b += [R(x0, y, x1 - x0, fh, fill=k.bg), L(x0, y, x0, y + fh, k.ink, 2.2), L(x1, y, x1, y + fh, k.ink, 2.2),
              R(x0 - 4, y - 2, x1 - x0 + 8, 4, fill=k.ink),
              T(x0 + 10, y + 17, name, k.ink, 10, weight=700, ls=.8), T(x1 - 9, y + 17, year, k.dim, 9, "end")]
    ry = g - 5 * fh - 44
    b += [R(x0, ry, x1 - x0, 44, fill="url(#wip)", stroke=k.amber, sw=1.2, dash="5 3"),
          scaffold(k, x0, ry, x1 - x0, 44),
          R(x0 + 8, ry + 8, 122, 29, fill=k.bg),
          T(x0 + 14, ry + 21, "REVORA", k.amber, 12, weight=800, ls=2),
          T(x0 + 14, ry + 33, "UNDER CONSTRUCTION", k.amber, 8, weight=700, ls=1.2),
          R(x0, ry - 34, x1 - x0, 34, stroke=k.faint, sw=1, dash="2 4"),
          T((x0 + x1) / 2, ry - 13, "NEXT", k.dim, 9, "middle", ls=3),
          crane(k, 806, g, 120, 622, 846, 690, 200),
          bubble(556, ry + 22, "1", "A-101", k, k.amber), L(571, ry + 22, 584, ry + 22, k.amber, .9),
          P(f"M592 {ry + 46}H586V{g}H592", k.ink, .9), bubble(556, 366, "2", "R-302", k), L(571, 366, 586, 366, k.ink, .9),
          bubble(556, 462, "3", "S-201", k), L(571, 460, 604, 450, k.ink, .9)]

    b.append(title_block(16, 528, 848, 56, [
        cell("PROJECT", "TUSHAR JOSHI · TJ-01", 220), cell("DRAWN", "T. JOSHI", 96),
        cell("CHECKED", "policy.py", 108), cell("SCALE", "NTS", 70), cell("REV", rev, 66, k.amber),
        cell("ISSUED", rv["date"], 112), cell("SHEET", "G-001", size=20)], k))
    return svg(W, H, k, "Sheet G-001, cover: Tushar Joshi, engineer under construction. Currently building REVORA.",
               "".join(b), BEACON)


def section(k: Ink, s: dict) -> str:
    W, H = 880, 830
    rv = s["revora"]
    rev = f'{rv["commits"]:02d}'
    bx0, bx1, g = 236, 596, 520
    b = [topbar(W, k, "DRAWING SET TJ  ·  SHEET A-101  ·  SECTION A–A THROUGH REVORA"),
         T(42, 104, "REVORA", k.indigo, 46, weight=800, ls=7, sans=True),
         T(44, 128, "REVENUE RECOVERY INFRASTRUCTURE", k.ink, 12, weight=700, ls=3),
         T(44, 148, "section through the whole stack: what's built, what's scaffolding, what isn't poured yet", k.dim, 11),
         T(836, 88, "STATUS", k.dim, 9, "end", ls=2),
         C(652, 104.5, 4.5, fill=k.amber), T(836, 109, "ACTIVE DEVELOPMENT", k.amber, 13, "end", 800, 1.5),
         T(836, 127, "not launched · payments simulated", k.dim, 10, "end"),
         R(206, g, 470, 152, fill="url(#earth)")]

    def room(y0, y1, name, desc, tests=None, fill=None, name_color=None):
        out = [R(bx0, y0, bx1 - bx0, y1 - y0, fill=fill or k.bg)]
        if fill:
            out.append(R(bx0 + 10, y0 + 8, 300, y1 - y0 - 16, fill=k.bg, opacity=.94))
        mid = (y0 + y1) / 2
        out += [T(bx0 + 16, mid - 3, name, name_color or k.ink, 11, weight=700, ls=1.5),
                T(bx0 + 16, mid + 12, desc, k.dim, 10)]
        if tests:
            out.append(tag(k, 552, mid, tests))
        return out

    above = [(304, 364, "PRODUCT SURFACES", "Next.js 14 · 12 app routes · 5 site pages", None, "L4"),
             (364, 416, "API", "FastAPI · 17 endpoints · idempotent execute", "7", "L3"),
             (416, 468, "SERVICES", "orchestration · structured audit log", "1", "L2"),
             (468, 520, "INTELLIGENCE", "XGBoost P(recovery) · expected-value engine", "4", "L1")]
    for y0, y1, name, desc, tests, lvl in above:
        b += room(y0, y1, name, desc, tests)
        b.append(T(606, (y0 + y1) / 2 + 3, lvl, k.dim, 9))
    b += room(520, 580, "FOUNDATION — DOMAIN + POLICY", "6 deterministic rules · AI cannot override", "7",
              fill="url(#concrete)")
    b += room(580, 624, "STORAGE", "InMemoryRepository · resets on restart", name_color=k.amber)
    for x in (504, 544, 584):
        b += [L(x, 583, x, 621, k.amber, 1.4), R(x - 6, 581.5, 12, 2.5, fill=k.amber), R(x - 6, 620, 12, 2.5, fill=k.amber)]
    b += [L(504, 583, 544, 621, k.amber, .8, "3 2"), L(544, 583, 584, 621, k.amber, .8, "3 2"),
          R(bx0, 624, bx1 - bx0, 40, fill=k.bg, stroke=k.faint, sw=1.2, dash="2 4"),
          T((bx0 + bx1) / 2, 648, "PostgresRepository — NOT YET POURED", k.dim, 10.5, "middle", 700, 1.2)]
    for lvl, y in (("B1", 553), ("B2", 605), ("B3", 647)):
        b.append(T(606, y, lvl, k.dim, 9))

    for y in (304, 364, 416, 468, 580, 624):
        b.append(R(bx0 - 5, y - 2.5, bx1 - bx0 + 10, 5, fill=k.ink))
    b += [L(bx0, 304, bx0, 490, k.ink, 2.6), L(bx0, 518, bx0, 624, k.ink, 2.6), L(bx1, 304, bx1, 624, k.ink, 2.6),
          L(bx0, 491, bx0, 517, k.amber, 1.4, "2 2"), L(190, g, 676, g, k.ink, 2)]

    b += [R(296, 254, 240, 50, fill="url(#wip)", stroke=k.amber, sw=1.2, dash="5 3"),
          scaffold(k, 296, 254, 240, 50),
          R(306, 261, 226, 36, fill=k.bg),
          T(314, 276, "AI COPILOT", k.amber, 11, weight=800, ls=1.5),
          T(314, 291, "rule-based answers · no LLM call yet", k.dim, 9.5),
          T(606, 283, "L5", k.dim, 9)]

    b += [T(44, 272, "SCAFFOLDING", k.amber, 9.5, weight=700, ls=1),
          T(44, 286, "partly fitted out — see P04", k.dim, 9.5), L(210, 278, 278, 278, k.dim, .8, "3 3"),
          R(200, 431, 32, 22, fill=k.bg, stroke=k.ink, sw=1.1), T(216, 445.5, "EXEC", k.ink, 7.5, "middle", 700),
          L(232, 442, bx0, 442, k.ink, 1.4), L(48, 442, 200, 442, k.amber, 1.4, "6 4"), arrow(42, 442, k, k.amber, "left"),
          T(44, 425, "PAYMENT RAILS — NOT CONNECTED", k.amber, 9.5, weight=700, ls=.6),
          T(44, 462, "SimulationProvider — a mock-up", k.dim, 9.5),
          T(44, 500, "ACCESS CONTROL — NOT FITTED", k.amber, 9.5, weight=700, ls=.6),
          T(44, 514, "no auth · single-tenant demo", k.dim, 9.5),
          T(44, 598, "TEMPORARY SHORING", k.amber, 9.5, weight=700, ls=1),
          T(44, 612, "permanent DB not poured — P01", k.dim, 9.5), L(222, 603, 236, 603, k.dim, .8, "3 3")]

    b.append(crane(k, 652, g, 178, 336, 722, 416, 234))
    lines = textwrap.wrap(rv["message"], 28, max_lines=2, placeholder=" …") + [""]
    b += [T(676, 224, "CRANE LOG — LAST LIFT", k.dim, 8.5, ls=1.5),
          T(676, 242, rv["date"], k.ink, 11.5, weight=700),
          T(676, 258, lines[0], k.dim, 9.5), T(676, 271, lines[1], k.dim, 9.5),
          T(676, 288, f'{rv["sha"]} · {rv["commits"]} public commits', k.dim, 9)]
    record = [("policy engine", 7), ("decision engine", 4), ("executor", 3), ("full pipeline", 1), ("API integration", 7)]
    b += [T(676, 326, "INSPECTION RECORD", k.dim, 8.5, ls=1.5), T(676, 340, "pytest · backend/tests", k.dim, 9)]
    for i, (name, n) in enumerate(record):
        b += [T(676, 362 + 18 * i, name, k.ink, 10), T(846, 362 + 18 * i, n, k.ink, 10, "end", 700)]
    b += [L(676, 452, 846, 452, k.faint), T(676, 470, "PASSING", k.green, 10.5, weight=700, ls=1.5),
          T(846, 470, sum(n for _, n in record), k.green, 12, "end", 800),
          T(676, 494, "frontend: no automated", k.dim, 9), T(676, 507, "tests yet — see P07", k.dim, 9)]

    b += [L(36, 682, 844, 682, k.faint), T(44, 702, "LEGEND", k.dim, 8.5, ls=2),
          R(44, 712, 26, 14, fill=k.bg, stroke=k.ink, sw=1.2), R(42, 710, 30, 3, fill=k.ink), T(78, 723, "BUILT", k.ink, 9.5),
          R(190, 712, 26, 14, fill="url(#wip)", stroke=k.amber, sw=1.1, dash="4 2"), T(224, 723, "STAND-IN / PARTIAL", k.ink, 9.5),
          R(362, 712, 26, 14, stroke=k.faint, sw=1.2, dash="2 3"), T(396, 723, "NOT BUILT", k.ink, 9.5),
          R(44, 734, 26, 14, fill="url(#concrete)", stroke=k.ink, sw=1.1), T(78, 745, "DETERMINISTIC — NO ML", k.ink, 9.5),
          tag(k, 226, 741, "n"), T(270, 745, "TESTS ON THAT LAYER", k.ink, 9.5),
          T(500, 702, "NOTES", k.dim, 8.5, ls=2),
          T(500, 720, "1  NOT A LAUNCHED PRODUCT — EXECUTION IS SIMULATED.", k.ink, 9.5),
          T(500, 735, "2  ALL TRANSACTIONS ARE SYNTHETIC DEMO DATA.", k.ink, 9.5),
          T(500, 750, "3  HOW ONE DECISION MOVES THROUGH IT: SEE A-102.", k.ink, 9.5)]
    b.append(title_block(16, 766, 848, 48, [
        cell("PROJECT", "REVORA — REVENUE RECOVERY INFRASTRUCTURE", 336, size=11.5), cell("DRAWN", "T. JOSHI", 90),
        cell("STATUS", "ACTIVE DEVELOPMENT", 170, k.amber, 11.5), cell("REV", rev, 60, k.amber),
        cell("ISSUED", rv["date"], 104), cell("SHEET", "A-101", size=19)], k))
    return svg(W, H, k, "Sheet A-101: REVORA drawn as a building section. Built and tested floors: product surfaces, API, "
               "services, intelligence, and a deterministic policy-engine foundation. Scaffolding: AI copilot. "
               "Not built: database, auth, live payment connection.", "".join(b), BEACON)


def decision(k: Ink, s: dict) -> str:
    W, H = 880, 610
    rv = s["revora"]
    rev = f'{rv["commits"]:02d}'
    b = [topbar(W, k, "DRAWING SET TJ  ·  SHEET A-102  ·  DETAIL 1 — DECISION PATH"),
         T(42, 100, "ONE DECISION, END TO END", k.ink, 28, weight=800, sans=True),
         T(44, 124, "how a revenue leak becomes an action — and who gets to say no", k.dim, 11.5)]
    for i, (c, label) in enumerate(((k.violet, "AI PROPOSAL"), (k.green, "ALLOWED BY POLICY"), (k.coral, "DOWNGRADED BY POLICY"))):
        b += [C(698, 86 + 16 * i, 4.5, fill=c), T(710, 89.5 + 16 * i, label, k.dim, 9, ls=1)]

    nodes = [("01  DETECT", ["4 leak types:", "payment · checkout", "renewal · invoice"]),
             ("02  CANDIDATES", ["a fixed subset", "of 5 actions", "per leak type"]),
             ("03  SCORE", ["p = P(xgb) × m(a)", "EV = p × amount", "  − cost − friction"]),
             ("04  PROPOSE", ["highest EV wins —", "still only a", "proposal"])]
    for i, (title, lines) in enumerate(nodes):
        x = 44 + 128 * i
        b += [R(x, 160, 112, 76, fill=k.bg, stroke=k.violet if i == 3 else k.ink, sw=1.2, rx=4),
              T(x + 10, 178, title, k.violet if i == 3 else k.ink, 10, weight=800, ls=.8)]
        b += [T(x + 10, 196 + 13 * j, ln, k.dim, 9) for j, ln in enumerate(lines)]
        if i < 3:
            b += [L(x + 112, 198, x + 126, 198, k.ink, 1.2), arrow(x + 128, 198, k)]
        b += [L(x + 56, 236, x + 56, 324, k.faint, 1, "3 3"), arrow(x + 56, 330, k, k.faint, "down")]
    b += [L(540, 198, 562, 198, k.ink, 1.2), arrow(566, 198, k),
          T(578, 142, "POLICY GATE", k.ink, 9, "middle", 800, 1.5),
          R(566, 150, 5, 100, fill=k.ink), R(585, 150, 5, 100, fill=k.ink)]
    for i in range(6):
        y = 160 + 16 * i
        b += [L(571, y, 585, y, k.ink, 1.8), T(594, y + 3, f"R{i + 1}", k.dim, 7)]
    b += [T(578, 266, "policy.py", k.dim, 9, "middle"),
          L(578, 272, 578, 324, k.faint, 1, "3 3"), arrow(578, 330, k, k.faint, "down"),
          P("M590 198H618V181H634", k.green, 1.4), arrow(640, 181, k, k.green),
          P("M618 198V265H634", k.coral, 1.4, dash="5 3"), arrow(640, 265, k, k.coral)]
    for y, color, title, lines in ((150, k.green, "05  ALLOWED → EXECUTE", ["idempotent · SimulationProvider", "→ recovered / not recovered"]),
                                   (234, k.coral, "05  DOWNGRADED → REROUTE", ["escalate → merchant review", "suppress → deliberate no-op"])):
        b += [R(640, y, 196, 62, fill=k.bg, stroke=color, sw=1.2, rx=4), T(650, y + 18, title, color, 10, weight=800, ls=.6),
              T(650, y + 36, lines[0], k.dim, 9), T(650, y + 50, lines[1], k.dim, 9),
              L(738, y + 62, 738, 324, k.faint, 1, "3 3") if y == 234 else ""]
    b += [arrow(738, 330, k, k.faint, "down"), L(44, 332, 836, 332, k.ink, 1.4),
          T(44, 352, "AUDIT LOG — every decision is written down, allowed or blocked", k.ink, 10.5, weight=700),
          T(44, 368, "DECISION_CREATED · POLICY_EVALUATED · ACTION_AUTHORIZED · ACTION_BLOCKED · EXECUTION_STARTED", k.dim, 9),
          T(44, 382, "EXECUTION_SUCCEEDED · EXECUTION_FAILED · ESCALATION_CREATED · SUPPRESSION_CREATED", k.dim, 9),
          C(0, 0, 5.5, fill=k.violet, cls="tok a"), C(0, 0, 5.5, fill=k.violet, cls="tok b")]

    b += [L(36, 402, 844, 402, k.faint), T(44, 424, "CANDIDATE MATRIX", k.dim, 8.5, ls=2),
          T(44, 438, "which actions are even considered, per leak type", k.dim, 9)]
    cols = ["RETRY", "LINK", "REMIND", "ESCAL", "SUPPR"]
    matrix = {"failed_payment": "RLMS", "abandoned_checkout": "MLS", "failed_subscription": "RLES", "overdue_invoice": "MLES"}
    for j, c in enumerate(cols):
        b.append(T(212 + 40 * j, 458, c, k.dim, 8, "middle", 700))
    for i, (leak, allowed) in enumerate(matrix.items()):
        y = 476 + 18 * i
        b.append(T(44, y + 3.5, leak, k.ink, 9.5))
        for j, code in enumerate("RLMES"):
            b.append(C(212 + 40 * j, y, 4.5, fill=k.ink) if code in allowed else C(212 + 40 * j, y, 2, stroke=k.faint, sw=1))
    rules = [("retry after 2 retries already", "escalate"), ("retry < 6h since the last event", "suppress"),
             ("retry, subscription failed > 2× in a row", "escalate"), ("link / reminder, 1 contact already today", "suppress"),
             ("anything but escalate, amount > ₹25,000", "escalate"), ("invoice more than 30 days overdue", "escalate")]
    b += [T(440, 424, "POLICY RULES", k.dim, 8.5, ls=2), T(440, 438, "deterministic · can only downgrade, never expand", k.dim, 9)]
    for i, (cond, result) in enumerate(rules):
        y = 460 + 16 * i
        b += [T(440, y, f"R{i + 1}", k.dim, 9.5, weight=700), T(468, y, cond, k.ink, 9.5),
              T(836, y, f"→ {result}", k.amber if result == "escalate" else k.dim, 9.5, "end", 700)]
    b.append(title_block(16, 554, 848, 40, [
        cell("PROJECT", "REVORA", 120), cell("DETAIL", "DECISION PATH", 160),
        cell("SOURCE", "decision_engine.py · policy.py", 250, size=11), cell("REV", rev, 60, k.amber),
        cell("ISSUED", rv["date"], 104), cell("SHEET", "A-102", size=17)], k))

    def path(name, color, exit_y, delay):
        return (f".{name}{{animation:{name} 10s linear {delay}s infinite}}"
                f"@keyframes {name}{{0%{{transform:translate(100px,198px);opacity:0;fill:{k.violet}}}"
                f"4%{{opacity:1}}36%{{transform:translate(578px,198px);fill:{k.violet}}}"
                f"40%{{transform:translate(578px,198px);fill:{color}}}44%{{transform:translate(618px,198px)}}"
                f"48%{{transform:translate(618px,{exit_y}px)}}53%{{transform:translate(662px,{exit_y}px);opacity:1;fill:{color}}}"
                f"58%{{transform:translate(662px,{exit_y}px);opacity:0;fill:{color}}}100%{{opacity:0;transform:translate(662px,{exit_y}px)}}}}")

    css = (".tok{opacity:0}" + path("a", k.green, 181, 0) + path("b", k.coral, 265, 5)
           + "@media (prefers-reduced-motion:reduce){.tok{animation:none}}")
    return svg(W, H, k, "Sheet A-102: how one REVORA decision flows. Detect, candidates, score by expected value, propose, "
               "then a deterministic policy gate with six rules either allows execution or downgrades to escalate or "
               "suppress. Every step is written to the audit log.", "".join(b), css)


def foundation(k: Ink, s: dict) -> str:
    W, H = 880, 600
    lc, rv = s["leetcode"], s["revora"]
    b = [topbar(W, k, "DRAWING SET TJ  ·  SHEET S-201  ·  FOUNDATION PLAN"),
         T(42, 100, "FOUNDATION — DSA", k.ink, 28, weight=800, sans=True),
         T(44, 124, "one pile per accepted LeetCode problem · pile depth = difficulty", k.dim, 11.5),
         T(836, 106, lc["total"], k.ink, 48, "end", 800, sans=True),
         T(836, 126, "PILES DRIVEN", k.dim, 9, "end", ls=2),
         T(422, 166, "EVERYTHING ELSE ON THESE SHEETS STANDS ON THIS", k.dim, 8.5, "middle", ls=2),
         R(44, 184, 792, 214, fill="url(#earth)"), R(44, 176, 756, 8, fill=k.ink)]
    groups = [("EASY", lc["easy"], 64), ("MEDIUM", lc["medium"], 128), ("HARD", lc["hard"], 192)]
    n = max(1, sum(c for _, c, _ in groups))
    pitch = min(7.0, (756 - 16 - 2 * 22) / n)
    pw = max(1.6, pitch * .5)
    x = 52.0
    for name, count, depth in groups:
        start = x
        for _ in range(count):
            b += [R(x, 184, pw, depth, fill=k.ink, opacity=.9), P(f"M{num(x)} {184 + depth}h{num(pw)}l{num(-pw / 2)} 4z", fill=k.ink)]
            x += pitch
        if count:
            cx = (start + x - pitch + pw) / 2
            label = f"{name} {count}"
            b += [R(cx - len(label) * 3.6 - 6, 184 + depth + 10, len(label) * 7.2 + 12, 16, fill=k.bg),
                  T(cx, 184 + depth + 22, label, k.ink, 10, "middle", 800, 1.5)]
        x += 22
    b += [L(816, 184, 816, 376, k.dim, .8)]
    for depth, label in ((64, "1×"), (128, "2×"), (192, "3×")):
        b += [L(811, 184 + depth, 821, 184 + depth, k.dim, .8), T(826, 188 + depth, label, k.dim, 9)]
    b.append(L(811, 184, 821, 184, k.dim, .8))

    cal = lc["calendar"]
    last = dt.date.fromisoformat(max(cal)) if cal else dt.date.fromisoformat(rv["date"])
    days = [last - dt.timedelta(days=89 - i) for i in range(90)]
    step = 792 / 90
    b += [T(44, 426, "POUR LOG", k.dim, 8.5, ls=2), T(120, 426, f"submissions per day · 90 days to {last.isoformat()}", k.dim, 9),
          L(44, 474, 836, 474, k.faint)]
    for i, d in enumerate(days):
        c = cal.get(d.isoformat(), 0)
        xx = 44 + step * i + 1.4
        if c:
            h = 6 + min(c, 12) / 12 * 30
            b.append(R(xx, 474 - h, step - 2.8, h, fill=k.amber if d == last else k.ink, opacity=.9))
        else:
            b.append(R(xx, 472.5, step - 2.8, 1.5, fill=k.faint))
        if d.day == 1:
            b += [L(xx, 474, xx, 480, k.dim, .8), T(xx + 2, 490, d.strftime("%b").upper(), k.dim, 8.5)]
    langs = " · ".join(f"{name} {count}" for name, count in lc["languages"][:3])
    b.append(T(44, 516, f'ACTIVE DAYS {lc["active_days"]} IN {lc["year"]}   ·   MAX STREAK {lc["max_streak"]}   ·   SOLVED IN  {langs}', k.ink, 10.5))
    b.append(title_block(16, 536, 848, 48, [
        cell("SOURCE", f"leetcode.com/u/{LC_USER} · public API", 280, size=11),
        cell("LAST ACTIVE", last.isoformat(), 116), cell("PRACTICE REPO", "DSA-in-Cpp · 21 C++ files", 214, size=11),
        cell("REV", f'{rv["commits"]:02d}', 60, k.amber), cell("SHEET", "S-201", size=19)], k))
    return svg(W, H, k, f'Sheet S-201: foundation plan. {lc["total"]} accepted LeetCode problems drawn as piles: '
               f'{lc["easy"]} easy, {lc["medium"]} medium, {lc["hard"]} hard, plus a 90-day activity log.', "".join(b))


def stair(k: Ink, s: dict) -> str:
    W, H = 880, 600
    rv = s["revora"]
    b = [topbar(W, k, "DRAWING SET TJ  ·  SHEET R-301  ·  STAIR SECTION"),
         T(42, 100, "HOW I GOT HERE", k.ink, 28, weight=800, sans=True),
         T(44, 124, "every public repo, one flight at a time — each tread bears on the one below", k.dim, 11.5),
         L(36, 500, 300, 500, k.ink, 1.6), R(36, 500, 264, 14, fill="url(#earth)"),
         P("M44 470H234V385H424V300H614V215H804V245L234 500H44Z", k.ink, 1.4, fill="url(#concrete)"),
         T(44, 240, "NOTES", k.dim, 8.5, ls=2),
         T(44, 258, "1  RISERS ARE DRAWN EQUAL. THE SCOPE IS NOT.", k.ink, 9.5),
         T(44, 273, "2  PRACTICE REPOS INCLUDED — A STAIR STARTS AT THE BOTTOM.", k.ink, 9.5)]
    for x, y in ((44, 470), (234, 385), (424, 300), (614, 215)):
        b += [L(x, y, x + 190, y, k.ink, 2.4), L(x + 190, y, x + 190, y - 85, k.ink, 1.4) if x < 614 else ""]
    treads = [
        (44, 470, "01 · FUNDAMENTALS", "OCT → DEC 2025", ["campus-apex — Java CRUD", "Java-Finance-Tracker",
                                                          "DSA-in-Cpp — 21 C++ files", "DBMS-SQL · Password-Manager"]),
        (234, 385, "02 · VISUALIZERS", "FEB → MAY 2026", ["PalindromeCheckerApp", "A* search visualizer", "3D-Shearing (CG site)"]),
        (424, 300, "03 · SHIPPED PRODUCT", "AUG 2026", ["DailyFlow — Electron+SQLite", "17 test files · installer",
                                                               "DailyFlow-Website"]),
        (614, 215, "04 · INFRASTRUCTURE", "SEP 2026 → NOW", ["REVORA — under construction", "FastAPI · XGBoost · Next.js",
                                                              "22 backend tests"])]
    for i, (x, y, title, when, items) in enumerate(treads):
        top = y - 22 - 13 * (len(items) + 1)
        live = i == 3
        b += [T(x + 8, top, title, k.amber if live else k.ink, 10.5, weight=800, ls=1),
              T(x + 8, top + 14, when, k.amber if live else k.dim, 9, ls=1.2)]
        b += [T(x + 8, top + 30 + 13 * j, it, k.ink, 9.5) for j, it in enumerate(items)]
    b += [P("M804 215V142H852", k.faint, 1.2, dash="2 4"), T(846, 134, "NEXT FLIGHT", k.dim, 8.5, "end", ls=1.5),
          P("M800 205l-8-8M800 205l-8 8", k.amber, 1.6), T(790, 209, "YOU ARE HERE", k.amber, 8.5, "end", 800, 1.2)]
    b.append(title_block(16, 536, 848, 48, [
        cell("PROJECT", "TUSHAR JOSHI · PUBLIC WORK", 260, size=11.5), cell("SOURCE", "github.com/tushar-cr7", 210, size=11),
        cell("REV", f'{rv["commits"]:02d}', 60, k.amber), cell("ISSUED", rv["date"], 110), cell("SHEET", "R-301", size=19)], k))
    return svg(W, H, k, "Sheet R-301: stair section of public work. Fundamentals (2025), visualizers (early 2026), "
               "first shipped product DailyFlow (August 2026), infrastructure: REVORA (now).", "".join(b))


STRIPS = {
    "g-000-index": ("G-000", "DRAWING INDEX", "every sheet in this set — the sheet numbers are links", "8 SHEETS", "ink"),
    "g-002-notes": ("G-002", "GENERAL NOTES", "how I build — these apply to every sheet in the set", "ISSUED", "ink"),
    "a-103-punch": ("A-103", "PUNCH LIST — REVORA", "open items before handover · nothing here is hidden", "8 OPEN", "amber"),
    "r-302-register": ("R-302", "AS-BUILT REGISTER", "everything public — and exactly what is in each repo", "AS-BUILT", "green"),
    "x-900-rfi": ("X-900", "REQUESTS FOR INFORMATION", "questions go to the engineer on site", "OPEN", "green"),
}


def strip(k: Ink, s: dict, key: str) -> str:
    W, H = 880, 60
    number, title, sub, status, color = STRIPS[key]
    c = k[color]
    cw = len(status) * 6.4 + 26
    body = (R(0, 0, W, H, fill=k.bg, rx=10) + R(0, 0, W, H, fill="url(#g2)", rx=10, opacity=.75)
            + R(8, 8, W - 16, H - 16, stroke=k.ink, sw=1.1, opacity=.8) + L(112, 8, 112, H - 8, k.ink, .8)
            + T(60, 37, number, k.ink, 17, "middle", 800) + T(128, 29, title, k.ink, 12.5, weight=800, ls=2)
            + T(128, 44, sub, k.dim, 9.5) + R(W - 22 - cw, 20, cw, 20, stroke=c, sw=1.2, rx=10)
            + T(W - 22 - cw / 2, 34, status, c, 9.5, "middle", 800, 1.2))
    return svg(W, H, k, f"Sheet {number}: {title.lower()}", body, framed=False)


def end_of_set(k: Ink, s: dict) -> str:
    W, H = 880, 60
    rev = f'{s["revora"]["commits"]:02d}'
    body = (R(0, 0, W, H, fill=k.bg, rx=10) + R(0, 0, W, H, fill="url(#g2)", rx=10, opacity=.75)
            + R(8, 8, W - 16, H - 16, stroke=k.ink, sw=1.1, opacity=.8)
            + T(W / 2, 29, "END OF SET", k.ink, 12.5, "middle", 800, 4)
            + T(W / 2, 45, f"REV {rev} — SUPERSEDED BY REVORA'S NEXT COMMIT", k.amber, 9.5, "middle", 700, 1.5))
    return svg(W, H, k, f"End of set. Revision {rev}, superseded by REVORA's next commit.", body, framed=False)


SHEETS = {
    "g-001-cover": cover, "a-101-revora-section": section, "a-102-decision-path": decision,
    "s-201-foundation": foundation, "r-301-stair": stair, "zz-end-of-set": end_of_set,
    **{key: (lambda key: lambda k, s: strip(k, s, key))(key) for key in STRIPS},
}


def main() -> None:
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    for key, fetch in (("revora", fetch_revora), ("leetcode", fetch_leetcode)):
        try:
            state[key] = fetch()
        except Exception as exc:  # network, rate limit, schema drift
            print(f"warn: {key}: {exc!r} — keeping last verified data", file=sys.stderr)
            if key not in state:
                sys.exit(f"no verified data for {key}; refusing to draw")
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    for theme, ink in INKS.items():
        (OUT / theme).mkdir(parents=True, exist_ok=True)
        for name, draw in SHEETS.items():
            (OUT / theme / f"{name}.svg").write_text(draw(ink, state), encoding="utf-8")
    print(f"issued {len(SHEETS)} sheets x {len(INKS)} inks - REV {state['revora']['commits']:02d}")


if __name__ == "__main__":
    main()
