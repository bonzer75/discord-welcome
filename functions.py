import io
import shutil
import requests
from PIL import Image, ImageDraw, ImageSequence, ImageFont


def create_image(url, text, output_path):
    nyancat = Image.open('resources/nyan-cat.gif')
    download_image(url)
    pfp = Image.open("resources/pfp.jpg")
    pfp = pfp.resize((256, 256))
    fuente = ImageFont.truetype("resources/arial.ttf", 45)
    # print(nyancat.size[1] / 2, nyancat.size[0] / 2.5)

    frames = []
    i = 0

    for frame in ImageSequence.Iterator(nyancat):

        frame_draw = ImageDraw.Draw(frame)
        frame_draw.text((200, 350), text, font=fuente)
        frame.paste(pfp, (300, 80))
        del frame_draw

        bytes_img = io.BytesIO()
        frame.save(bytes_img, format="GIF")
        frame = Image.open(bytes_img)

        if i > 1:
            frames.append(frame)
        i = i + 1

    frames[0].save(output_path, save_all=True, append_images=frames[1:])
    return True


def download_image(url_link):
    res = requests.get(url_link, stream=True, timeout=3)
    if res.status_code == 200:
        res.raw.decode_content = True
        with open("resources/pfp.jpg", "wb") as file:
            shutil.copyfileobj(res.raw, file)
    return

# testing
