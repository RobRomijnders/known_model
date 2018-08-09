import numpy as np
import matplotlib.pyplot as plt


def noisy(x):
    return x + 0.1 * np.random.rand()


def known_model(a, b, c, d, points):
    assert len(points.shape) == 1
    return np.exp(-noisy(a) * points) + noisy(b) * points + np.sin(noisy(c) * points) + noisy(d)

num_rows = 3
f, axarr = plt.subplots(num_rows)

for i, ax in enumerate(axarr):
    x = np.random.rand(9)
    ax.scatter(x, noisy(known_model(3, -2, 15, 2, x)))

for n_col, ax in enumerate(axarr):
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 5])
    if n_col != num_rows - 1:
        ax.get_xaxis().set_ticklabels([])
        # ax.get_yaxis().set_ticklabels([])
plt.tight_layout()
plt.subplots_adjust(wspace=0, hspace=0)

f.show()
plt.waitforbuttonpress()