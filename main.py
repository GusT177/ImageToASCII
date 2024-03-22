from PIL import Image

with Image.open("goofyahhchicken.jpg") as img:
    width, height = img.size
    simbols = "*+.#,"
    resize = 0.4
    WidthResized = int(width * resize)
    HeightResized = int(height * resize)
    asciiart = ''
    imgResized = img.resize((WidthResized, HeightResized))
    for y in range(HeightResized):
        for x in range(WidthResized):
            pixel = imgResized.getpixel((x, y))
            light = sum(pixel) / 3
            indexCharac = int((light / 255) * (len(simbols) - 1))
            asciiart += simbols[indexCharac]
        asciiart += '\n'

print(asciiart)
