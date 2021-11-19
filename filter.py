import numpy as np
from PIL import Image


def img_to_nparr(path):
    """
    Converting an image to np.array
    :param path: image path in string
    :return: np.array of pixels

    >>> img_to_nparr("test/test1.jpg")
    array([[[  0, 255,   0]]], dtype=uint8)
    """
    return np.array(Image.open(path))


def save_img_from_nparr(img, name):
    """
    Saving an image from np.array to an image file
    :param img: np.array to save
    :param name: filename to save
    """
    Image.fromarray(img).save(name)


def create_pixel_art(img, size, grayscale):
    """
    Create pixel art from an np.array image with pixel size - size
    :param img: image in type np.array
    :param size: pixel size
    :param grayscale: grayscale for image
    :return: b&w pixel art in type np.array

    >>> create_pixel_art(img_to_nparr('test/test2.jpg'), 10, 50)
    array([[[ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [100, 100, 100],
            [100, 100, 100]],
    <BLANKLINE>
           [[ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [100, 100, 100],
            [100, 100, 100]],
    <BLANKLINE>
           [[ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [100, 100, 100],
            [100, 100, 100]],
    <BLANKLINE>
           [[ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [100, 100, 100],
            [100, 100, 100]],
    <BLANKLINE>
           [[ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [100, 100, 100],
            [100, 100, 100]],
    <BLANKLINE>
           [[ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [100, 100, 100],
            [100, 100, 100]],
    <BLANKLINE>
           [[ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [100, 100, 100],
            [100, 100, 100]],
    <BLANKLINE>
           [[ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [100, 100, 100],
            [100, 100, 100]],
    <BLANKLINE>
           [[ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [100, 100, 100],
            [100, 100, 100]],
    <BLANKLINE>
           [[ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [ 50,  50,  50],
            [100, 100, 100],
            [100, 100, 100]],
    <BLANKLINE>
           [[100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [150, 150, 150],
            [150, 150, 150]],
    <BLANKLINE>
           [[100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [150, 150, 150],
            [150, 150, 150]],
    <BLANKLINE>
           [[100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [100, 100, 100],
            [150, 150, 150],
            [150, 150, 150]]], dtype=uint8)
    """
    for x in range(0, len(img), size):
        for y in range(0, len(img[1]), size):
            brightness = get_average_brightness(img, size, x, y)
            img[x: x + size, y: y + size] = brightness - brightness % grayscale
    return img


def get_average_brightness(img, size, x, y):
    """
    Getting the average brightness for a pixel
    :param img: image in type np.array
    :param size: radius around point for average brightness
    :param x: pixel x coordinate
    :param y: pixel y coordinate
    :return: average brightness in type int
    """
    return np.average(img[x: x + size, y: y + size])




# img = img_to_nparr(input('Write the path to the picture: '))
# size = int(input('Write the pixel size: '))
# grayscale = int(input('Write the step of grayscale: '))
# save_img_from_nparr(create_pixel_art(img, size, grayscale), 'res.jpg')
