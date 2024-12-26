# NOTE: Full generated AI code.

import colorsys

from PIL import Image


def is_color_approximately(rgb, target, tolerance=10):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(rgb, target))


def shift_hue(image, hue_shift):
    image = image.convert("RGBA")
    pixels = image.load()

    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if a > 0:
                if (
                    is_color_approximately((r, g, b), RED)
                    or is_color_approximately((r, g, b), WHITE)
                    or is_color_approximately((r, g, b), BLACK)
                ):
                    continue

                h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
                h = (h + hue_shift) % 1.0
                r, g, b = colorsys.hsv_to_rgb(h, s, v)
                pixels[x, y] = int(r * 255), int(g * 255), int(b * 255), a
    return image


def generate_hue_variations(image_path, output_path, steps=360):
    base_image = Image.open(image_path)
    width, height = base_image.size

    result_image = Image.new("RGBA", (width, height * steps))

    for i in range(steps):
        hue_shift = i / steps
        modified_image = shift_hue(base_image.copy(), hue_shift)
        result_image.paste(modified_image, (0, i * height))

    result_image.save(output_path)


input_image_path = "./assets/images/bird.png"
output_image_path = "./assets/images/birds.png"

generate_hue_variations(input_image_path, output_image_path)
