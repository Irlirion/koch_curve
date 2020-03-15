import numpy as np
import matplotlib.pyplot as plt


def get_threshold(Z: np.ndarray):
    return int(Z.mean())

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def fractal_dimension(Z: np.ndarray):
    # Only for 2d image
    assert (len(Z.shape) == 2)

    def boxcount(Z: np.ndarray, k: int):
        S = np.add.reduceat(
            np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
            np.arange(0, Z.shape[1], k), axis=1)

        # We count non-empty (0) and non-full boxes (k*k)
        return len(np.where((S > 0) & (S < k * k))[0])

    # Transform Z into a binary array
    Z = (Z < get_threshold(Z))
    plt.subplot(122)
    plt.imshow(Z, cmap="gray")

    # # Minimal dimension of image
    # p = min(Z.shape)
    #
    # # Greatest power of 2 less than or equal to p
    # n = 2 ** np.floor(np.log(p) / np.log(2))
    #
    # # Extract the exponent
    # n = int(np.log(n) / np.log(2))

    # Build successive box sizes (from 2**n down to 2**1)
    sizes = 2 ** np.arange(4, 1, -1)

    # Actual box counting with decreasing size
    counts = []
    for size in sizes:
        counts.append(boxcount(Z, size))
    # Fit the successive log(sizes) with log (counts)
    coeffs = np.polyfit(np.log(sizes), np.log(counts), 1)
    return -coeffs[0]


if __name__ == '__main__':
    I = plt.imread("town.jpg")
    I = rgb2gray(I)
    plt.subplot(121)
    plt.imshow(I, cmap="gray")
    print("Minkowski–Bouligand dimension (computed): ", fractal_dimension(I))
