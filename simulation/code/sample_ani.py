import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def update2(k, fig_title, coef):
    plt.cla()
    x = np.arange(xstart+k*xdt, xend+k*xdt, xdt)
    y = np.exp(-coef*(np.sin(x)**2))*np.cos(x)
    plt.plot(x, color='r')
    plt.title(fig_title, 'Frame k=' + str(k))
    plt.ylim(-1.2, 1.2)


ani = animation.FuncAnimation(fig, update2(), fargs=('Animation', 5.0)\
                                interval = 10, frames = 150, repeat = False)
