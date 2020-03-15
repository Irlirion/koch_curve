import koch
import fractal_demension as fd

if __name__ == '__main__':
    n = int(input("Введите ширину экрана для кривой Коха: "))

    points = koch.koch(n)
    img = koch.get_image(
                koch.get_prep_xy(
                   points
                )
            )
    x, y = koch.get_prep_xy(points)
    koch.plot(x, y)
    koch.imsave(str(n) + '.png', img)

    print(
        "Minkowski–Bouligand dimension (computed): ",
        fd.fractal_dimension(
            img
        )
    )

