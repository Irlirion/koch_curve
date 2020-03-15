import math
import numpy as np
from matplotlib import pyplot as plt

angles = [math.radians(60 * x) for x in range(6)]
sines = [math.sin(x) for x in angles]
cosin = [math.cos(x) for x in angles]


def L(angle, coords, jump):
    return (angle + 1) % 6


def R(angle, coords, jump):
    return (angle + 4) % 6


def F(angle, coords, jump):
    if angle == 0:
        for _ in range(jump):
            coords.append(
                ((coords[-1][0] + 1),
                 (coords[-1][1])))
    elif angle == 3:
        for _ in range(jump):
            coords.append(
                ((coords[-1][0] - 1),
                 (coords[-1][1])))
    else:
        for _ in range(jump):
            coords.append(
                ((coords[-1][0] + jump * cosin[angle]),
                 (coords[-1][1] + jump * sines[angle])))
    return angle


decode = dict(L=L, R=R, F=F)


def koch(width, start_pos=(0, 0)):
    pathcodes = "F"
    steps = int(np.log(width/2.66804) / np.log(3))
    print("Порядок: " + str(steps))
    for i in range(steps):
        pathcodes = pathcodes.replace("F", "FLFRFLF")

    # jump = float(length) / (3 ** steps)
    jump = 2
    coords = [start_pos]
    angle = 0

    for move in pathcodes:
        angle = decode[move](angle, coords, jump)

    return coords


def get_prep_xy(points):
    x = [int(i[0]) for i in points]
    y = [round(i[1] / (0.8660254037844386 * 2)) for i in points]

    return x, y


def plot(x, y, *args, **kwargs):
    plt.plot(x, y, *args, **kwargs)
    plt.gca().set_aspect('equal')
    plt.show()


def get_image(xy: tuple):
    x, y = xy
    img = np.ones((max(x) + 1, max(y) + 1), dtype='B')
    for i, j in zip(x, y):
        img[-(i + 1)][-(j + 1)] = 0
    img = img.T
    return img


def imsave(filename, img):
    plt.imsave(filename, img, cmap='gray')


if __name__ == '__main__':
    from fractal_demension import fractal_dimension

    width = 1000
    points = koch(width)
    print(points[:10])

    x = [int(i[0]) for i in points]
    y = [round(i[1] / (0.8660254037844386 * 2)) for i in points]
    print(x[:10])
    print(y[:10])
    plt.plot(x, y)
    plt.gca().set_aspect('equal')
    plt.show()

    img = np.ones((max(x) + 1, max(y) + 1))
    print(img.shape)
    for i, j in zip(x, y):
        img[-(i + 1)][-(j + 1)] = 0
    img = img.T
    plt.imsave('img.png', img, cmap='gray')

    print(fractal_dimension(img * 255))
