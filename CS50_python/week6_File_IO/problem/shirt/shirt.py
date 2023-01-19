
# CS50 P-Shirt
# наложение png изображения с альфа слоем на jpg
# Harvard / cs50p / python
# problem set week 6  https://cs50.harvard.edu/python/2022/psets/6/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com
import sys
from PIL import Image, ImageOps

overlay = 'shirt.png'
valid_ex = ('jpeg', 'jpg', 'png')


def main():

    path1, path2 = get_path()
    image_resized = resize(path1)
    final_image = merge_image(image_resized, overlay)
    save_image_to_jpg(final_image, path2)


def get_path():
    _, ex1 = sys.argv[1].lower().split('.')
    _, ex2 = sys.argv[2].lower().split('.')

    if len(sys.argv) != 3:
        print('Not correct command-line arguments ')
        sys.exit(1)

    elif ex1 == ex2 and ex2.endswith(valid_ex):
        return sys.argv[1], sys.argv[2]

    else:
        print('file ex not valid')
        sys.exit(1)


def resize(file_path):
    try:
        im = Image.open(file_path)
        im = ImageOps.fit(im, (600, 600))

    except FileNotFoundError:
        print('File not found')
        sys.exit()

    return im


def merge_image(im1, im2):
    im2 = Image.open(im2)
    im1.paste(im2, mask=im2)
    return im1


def save_image_to_jpg(im, path):
    im.save(path)


if __name__ == '__main__':
    main()
