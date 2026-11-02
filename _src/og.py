"""Рисует картинку-превью для ссылок og.png (1200×630) в пиксельном стиле.

Запуск из корня репозитория:  python3 _src/og.py
Шрифт нарисован вручную (5×7), внешние файлы не нужны.
"""
import os
import random
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1200, 630

BG, PANEL, LINE, SLATE = "#1a1c2c", "#262b44", "#333c57", "#566c86"
TEXT, MUTED, ACCENT, GREEN = "#f4f4f4", "#bccfdb", "#ffcd75", "#a7f070"

G = {
    # строчные для логотипа
    "b": ["X....", "X....", "XXXX.", "X...X", "X...X", "X...X", "XXXX."],
    "o": [".....", ".....", ".XXX.", "X...X", "X...X", "X...X", ".XXX."],
    "g": [".....", ".....", ".XXXX", "X...X", "X...X", "X...X", ".XXXX", "....X", "XXXX."],
    "u": [".....", ".....", "X...X", "X...X", "X...X", "X..XX", ".XX.X"],
    "s": [".....", ".....", ".XXXX", "X....", ".XXX.", "....X", "XXXX."],
    "p": [".....", ".....", "XXXX.", "X...X", "X...X", "X...X", "XXXX.", "X....", "X...."],
    "e": [".....", ".....", ".XXX.", "X...X", "XXXXX", "X....", ".XXX."],
    "d": ["....X", "....X", ".XXXX", "X...X", "X...X", "X...X", ".XXXX"],
    "v": [".....", ".....", "X...X", "X...X", "X...X", ".X.X.", "..X.."],
    ".": [".....", ".....", ".....", ".....", ".....", ".XX..", ".XX.."],
    # прописные для подписей
    "A": [".XXX.", "X...X", "X...X", "XXXXX", "X...X", "X...X", "X...X"],
    "B": ["XXXX.", "X...X", "X...X", "XXXX.", "X...X", "X...X", "XXXX."],
    "C": [".XXX.", "X...X", "X....", "X....", "X....", "X...X", ".XXX."],
    "D": ["XXXX.", "X...X", "X...X", "X...X", "X...X", "X...X", "XXXX."],
    "E": ["XXXXX", "X....", "X....", "XXXX.", "X....", "X....", "XXXXX"],
    "G": [".XXX.", "X...X", "X....", "X.XXX", "X...X", "X...X", ".XXXX"],
    "I": ["XXXXX", "..X..", "..X..", "..X..", "..X..", "..X..", "XXXXX"],
    "L": ["X....", "X....", "X....", "X....", "X....", "X....", "XXXXX"],
    "M": ["X...X", "XX.XX", "X.X.X", "X.X.X", "X...X", "X...X", "X...X"],
    "N": ["X...X", "XX..X", "X.X.X", "X..XX", "X...X", "X...X", "X...X"],
    "O": [".XXX.", "X...X", "X...X", "X...X", "X...X", "X...X", ".XXX."],
    "R": ["XXXX.", "X...X", "X...X", "XXXX.", "X.X..", "X..X.", "X...X"],
    "S": [".XXXX", "X....", "X....", ".XXX.", "....X", "....X", "XXXX."],
    "T": ["XXXXX", "..X..", "..X..", "..X..", "..X..", "..X..", "..X.."],
    "V": ["X...X", "X...X", "X...X", "X...X", "X...X", ".X.X.", "..X.."],
    "W": ["X...X", "X...X", "X...X", "X.X.X", "X.X.X", "XX.XX", "X...X"],
    "8": [".XXX.", "X...X", "X...X", ".XXX.", "X...X", "X...X", ".XXX."],
    "-": [".....", ".....", ".....", "XXXXX", ".....", ".....", "....."],
    "·": [".....", ".....", ".....", "..X..", ".....", ".....", "....."],
    " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
}


def text_width(s, scale):
    return len(s) * 6 * scale - scale


def draw_text(d, x, y, s, scale, color, shadow=None):
    for i, ch in enumerate(s):
        glyph = G[ch]
        for gy, row in enumerate(glyph):
            for gx, px in enumerate(row):
                if px == "X":
                    cx = x + (i * 6 + gx) * scale
                    cy = y + gy * scale
                    if shadow:
                        d.rectangle([cx + scale, cy + scale, cx + 2 * scale - 1, cy + 2 * scale - 1], fill=shadow)
                    d.rectangle([cx, cy, cx + scale - 1, cy + scale - 1], fill=color)


AVATAR = [
    "...HHHHHH...",
    "..HHHHHHHH..",
    "..HSSSSSSH..",
    "..SKKSSKKS..",
    "..SSSSSSSS..",
    "..SSESSESS..",
    "...SSMMSS...",
    "..BBBBBBBB..",
    ".BBBBBBBBBB.",
    ".SBBBBBBBBS.",
    "..LL....LL..",
    ".WWW....WWW.",
]
APAL = {"H": "#3b2416", "K": "#0d0d0d", "S": "#f2c39b", "E": "#1a1c2c",
        "M": "#b13e53", "B": "#1f2a5c", "L": "#1a1c2c", "W": "#f4f4f4"}


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # звёзды
    rnd = random.Random(7)
    for i in range(40):
        s = 8 if rnd.random() > 0.7 else 4
        x, y = rnd.randrange(0, W - 8), rnd.randrange(0, H - 8)
        if (40 <= x <= 470 and 90 <= y <= 540) or (480 <= x <= 1100 and 130 <= y <= 530):
            continue
        d.rectangle([x, y, x + s - 1, y + s - 1], fill=[TEXT, ACCENT, "#73eff7", GREEN][i % 4])

    # карточка с аватаром
    cx, cy, cw, ch = 72, 115, 368, 400
    d.rectangle([cx + 10, cy + 10, cx + cw + 9, cy + ch + 9], fill="#000000")
    d.rectangle([cx, cy, cx + cw - 1, cy + ch - 1], fill=TEXT)
    d.rectangle([cx + 6, cy + 6, cx + cw - 7, cy + ch - 7], fill=PANEL)
    fx, fy = cx + 28, cy + 28
    d.rectangle([fx, fy, fx + 311, fy + 343], fill=SLATE)
    px = 24
    ax, ay = fx + (312 - 12 * px) // 2, fy + 344 - 12 * px
    for r, row in enumerate(AVATAR):
        for c, ch_ in enumerate(row):
            if ch_ != ".":
                d.rectangle([ax + c * px, ay + r * px, ax + (c + 1) * px - 1, ay + (r + 1) * px - 1], fill=APAL[ch_])

    # тексты справа
    tx = 500
    draw_text(d, tx, 150, "VIBE-CODER · WARSAW", 4, GREEN)
    draw_text(d, tx, 222, "boguspoe.dev", 8, ACCENT, shadow="#000000")
    draw_text(d, tx, 340, "WEBSITES · TELEGRAM BOTS", 4, TEXT)
    draw_text(d, tx, 390, "AI AGENTS · N8N", 4, TEXT)

    # кнопка
    bx, by = tx, 452
    label = "START GAME"
    bw, bh = text_width(label, 3) + 48, 21 + 40
    d.rectangle([bx + 8, by + 8, bx + bw + 7, by + bh + 7], fill="#000000")
    d.rectangle([bx, by, bx + bw - 1, by + bh - 1], fill=TEXT)
    d.rectangle([bx + 5, by + 5, bx + bw - 6, by + bh - 6], fill=ACCENT)
    draw_text(d, bx + 24, by + 20, label, 3, BG)

    # ЭЛТ-полоски
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(over)
    for y in range(0, H, 4):
        od.rectangle([0, y, W, y + 1], fill=(0, 0, 0, 30))
    img = Image.alpha_composite(img.convert("RGBA"), over).convert("RGB")

    # рамка
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, 11], fill=LINE)
    d.rectangle([0, H - 12, W - 1, H - 1], fill=LINE)

    out = os.path.join(ROOT, "og.png")
    img.save(out, optimize=True)
    print("сохранено:", out)


if __name__ == "__main__":
    main()
