from typing import Callable
from mss.windows import MSS
import pygetwindow as gw
import PIL.Image as Image

cursor_y_offset = 1 / 288


def get_img(mss_: MSS, window: gw.Window) -> Image.Image:
    coords = {"top": window.top, "left": window.left, "width": window.width, "height": window.height}
    img = mss_.grab(coords)
    return Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")


def load_mss() -> (Callable[[], Image.Image], Callable[[MSS], None]):
    window = gw.getWindowsWithTitle("Valheim")[0]
    mss_ = MSS()
    return (lambda: get_img(mss_, window)), mss_.close


def heuristic_is_copper(image: Image.Image) -> bool:
    rgb = image.convert("RGB")

    center_x = rgb.width // 2
    center_y = rgb.height // 2

    offset_y = center_y - rgb.height * cursor_y_offset

    r, g, b = rgb.getpixel((center_x, offset_y))

    if r <= 160 or g <= 160:
        # cursor is not yellow, not possible to be copper node
        return False
    else:
        # could do OCR here but let's first just return True and see how it goes
        return True
