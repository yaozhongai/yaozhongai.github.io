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
draw.text((144, 220), "王耀中 · AI 算法工程师", font=font(FONT_CN_BOLD, 76), fill="#161616")
draw.text(
    (144, 410),
    "多模态大模型 · Agent · 算法工程化",
    font=font(FONT_CN, 50),
    fill="#5b5b5b",
)

draw.line((144, 700, 2256, 700), fill="#dfe6ef", width=2)

draw.text((144, 775), "从现场感知到智能处置", font=font(FONT_CN_BOLD, 68), fill="#161616")
draw.text(
    (144, 900),
    "Agent、多模态、边缘推理与算法工程化实践。",
    font=font(FONT_CN, 42),
    fill="#5b5b5b",
)

pill(draw, (144, 1030), "Agent 系统", "#dbeafe", "#1d4ed8")
pill(draw, (430, 1030), "多模态感知", "#dff5f2", "#0f766e")
pill(draw, (792, 1030), "边缘推理", "#e9e5ff", "#6d28d9")
pill(draw, (1074, 1030), "工程落地", "#f2eadf", "#9a5b18")

image.save(OUT, format="PNG", optimize=True)
print(OUT)
