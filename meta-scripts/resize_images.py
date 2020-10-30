import os
from PIL import Image


def main():
    new_width = 680
    dirname = "../app/static/expose"
    images = os.listdir(dirname)
    for image in images:
        fp = os.path.join(dirname, image)
        img = Image.open(fp)
        new_height = new_width * img.height // img.width
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(fp)