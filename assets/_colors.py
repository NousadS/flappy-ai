# NOTE: Full generated AI code.

from PIL import Image

def extract_unique_colors(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = list(image.getdata())
    unique_colors = set(pixels)
    
    for color in unique_colors:
        print(color)

image_path = "./assets/images/colors.png"

extract_unique_colors(image_path)
