"""Composite the approved catfish into the badge frame and set banner type."""

from __future__ import annotations

import math
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FISH_PATH = ROOT / "flathead-catfish-vintage-screenprint.png"
BADGE_PATH = ROOT / "badge-frame.png"
OUT_PATH = ROOT / "badge.png"
FONT_SLAB = ROOT / "fonts" / "AlfaSlabOne-Regular.ttf"

OAT = (237, 228, 208, 255)
SLATE = (46, 74, 82, 255)
WHITE_RGB = np.array([255.0, 255.0, 255.0])
RUST_RGB = np.array([168.0, 68.0, 42.0])


def flood_knockout_white(im: Image.Image, threshold: float = 18.0) -> Image.Image:
    """Remove the white background by flooding from the edges. Keeps cream ink."""
    rgba = im.convert("RGBA")
    arr = np.array(rgba)
    rgb = arr[:, :, :3].astype(np.float32)
    h, w = rgb.shape[:2]
    dist = np.sqrt(((rgb - WHITE_RGB) ** 2).sum(axis=2))
    is_bg = dist < threshold

    visited = np.zeros((h, w), dtype=bool)
    q = deque()
    for x in range(w):
        if is_bg[0, x]:
            q.append((x, 0))
            visited[0, x] = True
        if is_bg[h - 1, x]:
            q.append((x, h - 1))
            visited[h - 1, x] = True
    for y in range(h):
        if is_bg[y, 0]:
            q.append((0, y))
            visited[y, 0] = True
        if is_bg[y, w - 1]:
            q.append((w - 1, y))
            visited[y, w - 1] = True

    while q:
        x, y = q.popleft()
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < w and 0 <= ny < h and not visited[ny, nx] and is_bg[ny, nx]:
                visited[ny, nx] = True
                q.append((nx, ny))

    alpha = arr[:, :, 3].astype(np.float32)
    alpha[visited] = 0
    # Soft fringe: fade remaining near-white edge pixels
    fringe = (~visited) & (dist < 28)
    fade = np.clip((dist - 8) / 20.0, 0, 1)
    alpha[fringe] *= fade[fringe]
    arr[:, :, 3] = alpha.astype(np.uint8)
    return Image.fromarray(arr, "RGBA")


def crop_content(im: Image.Image, pad: int = 8) -> Image.Image:
    alpha = np.array(im.split()[-1])
    ys, xs = np.where(alpha > 12)
    x0, x1 = max(0, int(xs.min()) - pad), min(im.width, int(xs.max()) + pad + 1)
    y0, y1 = max(0, int(ys.min()) - pad), min(im.height, int(ys.max()) + pad + 1)
    return im.crop((x0, y0, x1, y1))


def rust_solidity(badge_rgb: np.ndarray) -> np.ndarray:
    dist = np.sqrt(((badge_rgb.astype(np.float32) - RUST_RGB) ** 2).sum(axis=2))
    # 1 where solid rust, 0 where not
    return np.clip((55 - dist) / 40.0, 0, 1)


def condense(glyph: Image.Image, scale_x: float) -> Image.Image:
    if scale_x == 1:
        return glyph
    w, h = glyph.size
    return glyph.resize((max(1, int(round(w * scale_x))), h), Image.Resampling.LANCZOS)


def render_glyph(
    ch: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int, int],
    scale_x: float,
    pad: int = 8,
) -> Image.Image:
    if ch == " ":
        space_w = int(font.getlength("H") * 0.38 * scale_x)
        return Image.new("RGBA", (max(space_w, 1), font.size + pad * 2), (0, 0, 0, 0))
    dummy = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    draw = ImageDraw.Draw(dummy)
    x0, y0, x1, y1 = draw.textbbox((0, 0), ch, font=font)
    g = Image.new("RGBA", (x1 - x0 + pad * 2, y1 - y0 + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(g).text((pad - x0, pad - y0), ch, font=font, fill=fill)
    return condense(g, scale_x)


def draw_text_on_arc(
    canvas: Image.Image,
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int, int],
    arc_cx: float,
    arc_cy: float,
    radius: float,
    start_phi: float,
    end_phi: float,
    *,
    up_outward: bool,
    scale_x: float = 0.90,
    tracking: float = 0.04,
) -> None:
    """Place capitals along an arc. phi is clockwise-from-up for top, from-down for bottom.

    For top banners (up_outward=True): phi=0 is straight up from (arc_cx, arc_cy).
    For bottom banners (up_outward=False): phi=0 is straight down from (arc_cx, arc_cy).
    """
    glyphs = [render_glyph(ch, font, fill, scale_x) for ch in text]
    widths = [g.size[0] for g in glyphs]
    # tracking as a fraction of typical glyph width
    typical = max(font.size * scale_x * 0.55, 1)
    gaps = [typical * tracking] * (len(text) - 1) + [0]
    total = sum(widths) + sum(gaps[:-1])

    arc_len = abs(end_phi - start_phi) * radius
    # If the string is shorter than the arc, center it; if longer, it will clip — caller sizes font.
    extra = max(arc_len - total, 0)
    pos = extra / 2.0

    for glyph, w, gap in zip(glyphs, widths, gaps):
        mid = pos + w / 2.0
        t = mid / arc_len if arc_len else 0.5
        phi = start_phi + t * (end_phi - start_phi)

        if up_outward:
            x = arc_cx + radius * math.sin(phi)
            y = arc_cy - radius * math.cos(phi)
            ux, uy = (x - arc_cx), (y - arc_cy)
        else:
            x = arc_cx + radius * math.sin(phi)
            y = arc_cy + radius * math.cos(phi)
            ux, uy = (arc_cx - x), (arc_cy - y)

        mag = math.hypot(ux, uy) or 1.0
        ux, uy = ux / mag, uy / mag
        angle = math.degrees(math.atan2(ux, -uy))

        rotated = glyph.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
        px = int(round(x - rotated.width / 2))
        py = int(round(y - rotated.height / 2))
        canvas.alpha_composite(rotated, (px, py))
        pos += w + gap


def apply_banner_wear(text_layer: Image.Image, solidity: np.ndarray) -> Image.Image:
    """Let existing screen-print holes in the rust banners eat into the lettering."""
    arr = np.array(text_layer)
    alpha = arr[:, :, 3].astype(np.float32)
    wear = 0.35 + 0.65 * solidity
    # Fine grain so type is not perfectly digital
    rng = np.random.default_rng(2027)
    grain = rng.normal(1.0, 0.06, alpha.shape).astype(np.float32)
    grain = np.clip(grain, 0.82, 1.12)
    alpha *= wear * grain
    arr[:, :, 3] = np.clip(alpha, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, "RGBA")


def main() -> None:
    badge = Image.open(BADGE_PATH).convert("RGBA")
    fish = crop_content(flood_knockout_white(Image.open(FISH_PATH)))

    W, H = badge.size
    cx, cy = W / 2.0, H / 2.0

    # Inner cream radius is ~313. Keep the whole fish inside with a little air.
    inner_r = 300.0
    max_w = inner_r * 2 - 28
    max_h = 510.0  # stay clear of the banners
    scale = min(max_w / fish.width, max_h / fish.height)
    new_size = (max(1, int(round(fish.width * scale))), max(1, int(round(fish.height * scale))))
    fish = fish.resize(new_size, Image.Resampling.LANCZOS)

    fx = int(round(cx - fish.width / 2))
    fy = int(round(cy - fish.height / 2) + 6)  # optical center, slightly low
    badge.alpha_composite(fish, (fx, fy))

    font_banner = ImageFont.truetype(str(FONT_SLAB), 56)
    font_loc = ImageFont.truetype(str(FONT_SLAB), 22)

    text_layer = Image.new("RGBA", badge.size, (0, 0, 0, 0))

    # Fitted midlines of the rust ribbons (see composite notes).
    # Top ribbon ~ center (513.2, 779.2) r=677.8, usable ±0.36 rad from peak.
    draw_text_on_arc(
        text_layer,
        "SUSQUEHANNA",
        font_banner,
        OAT,
        arc_cx=513.2,
        arc_cy=779.2,
        radius=677.8,
        start_phi=-0.36,
        end_phi=0.36,
        up_outward=True,
        scale_x=0.88,
        tracking=0.05,
    )
    # Bottom ribbon ~ center (512.9, 162.6) r=748.8
    draw_text_on_arc(
        text_layer,
        "CATFISH CLASSIC",
        font_banner,
        OAT,
        arc_cx=512.9,
        arc_cy=162.6,
        radius=748.8,
        start_phi=-0.44,
        end_phi=0.44,
        up_outward=False,
        scale_x=0.86,
        tracking=0.045,
    )

    badge_rgb = np.array(badge.convert("RGB"))
    text_layer = apply_banner_wear(text_layer, rust_solidity(badge_rgb))
    badge.alpha_composite(text_layer)

    # Location line under the bottom ribbon, outside the ring.
    loc = "LONG LEVEL, PA"
    loc_layer = Image.new("RGBA", badge.size, (0, 0, 0, 0))
    glyphs = [render_glyph(ch, font_loc, SLATE, 0.92, pad=1) for ch in loc]
    gap = 1
    total_w = sum(g.width for g in glyphs) + gap * (len(glyphs) - 1)
    total_h = max(g.height for g in glyphs)
    tmp = Image.new("RGBA", (total_w, total_h), (0, 0, 0, 0))
    x = 0
    for g in glyphs:
        tmp.alpha_composite(g, (x, (total_h - g.height) // 2))
        x += g.width + gap
    lx = int(round(cx - tmp.width / 2))
    ly = H - tmp.height - 4
    loc_layer.alpha_composite(tmp, (lx, ly))
    loc_arr = np.array(loc_layer)
    rng = np.random.default_rng(11)
    grain = rng.normal(1.0, 0.05, loc_arr[:, :, 3].shape)
    loc_arr[:, :, 3] = np.clip(loc_arr[:, :, 3].astype(np.float32) * np.clip(grain, 0.85, 1.1), 0, 255).astype(np.uint8)
    badge.alpha_composite(Image.fromarray(loc_arr, "RGBA"))

    # Keep a clean white square field around the badge (no drop shadow).
    bg = Image.new("RGB", badge.size, (255, 255, 255))
    bg.paste(badge, mask=badge.split()[-1])
    bg.save(OUT_PATH, "PNG", optimize=True)
    print(f"wrote {OUT_PATH} {bg.size} fish_scale={scale:.3f} fish_px={new_size} at ({fx},{fy})")


if __name__ == "__main__":
    main()
