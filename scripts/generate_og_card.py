"""Generate the social sharing card with deterministic typography."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "og-card.png"
W, H = 2400, 1260

FONT_CN = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_CN_BOLD = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_LATIN_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


def pill(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, bg: str, fg: str) -> None:
    x, y = xy
    label_font = font(FONT_CN_BOLD, 44)
    left, top, right, bottom = draw.textbbox((0, 0), text, font=label_font)
    text_w = right - left
    text_h = bottom - top
    width = text_w + 72
    height = 88
    draw.rounded_rectangle((x, y, x + width, y + height), radius=44, fill=bg)
    draw.text((x + 36, y + (height - text_h) / 2 - top), text, font=label_font, fill=fg)


image = Image.new("RGB", (W, H), "#f8fafc")
draw = ImageDraw.Draw(image)

# Brand rail and restrained background geometry.
draw.rectangle((0, 0, 16, H), fill="#2563eb")
draw.ellipse((1690, -340, 2630, 600), fill="#eef4ff")
draw.ellipse((1780, -250, 2540, 510), outline="#dce8ff", width=5)

draw.text((144, 130), "yaozhongai.github.io", font=font(FONT_LATIN_BOLD, 42), fill="#8a8a8a")
draw.text((144, 220), "王耀中", font=font(FONT_CN_BOLD, 132), fill="#161616")
draw.text(
    (144, 445),
    "大模型应用算法工程师（LLM Agent · RAG · 边缘智能）",
    font=font(FONT_CN, 54),
    fill="#5b5b5b",
)

draw.line((144, 700, 2256, 700), fill="#dfe6ef", width=2)

draw.text((144, 775), "OfferCheck", font=font(FONT_LATIN_BOLD, 72), fill="#161616")
draw.text((665, 790), "求职机会核验 Agent", font=font(FONT_CN_BOLD, 48), fill="#2563eb")
draw.text(
    (144, 900),
    "自主调查一次具体机会，输出三级风险判断与可追溯证据链——无证据，不裁定。",
    font=font(FONT_CN, 42),
    fill="#5b5b5b",
)

pill(draw, (144, 1030), "靠谱", "#dcfce7", "#15803d")
pill(draw, (355, 1030), "存疑", "#fef3c7", "#b45309")
pill(draw, (566, 1030), "大概率有坑", "#fee2e2", "#b91c1c")

image.save(OUT, format="PNG", optimize=True)
print(OUT)
