from os import path
from sys import exit
from pygame import image


def load_image(name):
    fullname = path.join('data\images', name)
    # Если файл не существует, то выходим
    if not path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit()
    img = image.load(fullname)
    return img
