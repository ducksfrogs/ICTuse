import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import cartopy.crs as ccrs


def update(k, fig_title):
    plt.cla()
    ax = plt.axes(projection=ccrs.Orthographic(central_longitude=(-k),central_latitude=0))
    ax.coastlines()
    plt.title(fig_title)


fig = plt.figure(figsize=(6,2))
x = np.arange(0, 10, 0.1)


def update(k, fig_title, Amp):
    plt.cla()
    y = Amp*np.sin(x-k)
    plt.plot(x, y, 'r')
    plt.xlim(0, 10)
    plt.ylim(-1.2*Amp, 1.2*Amp)
    plt.title(fig_title + 'Frame k =' + str(k) )


ani = animation.FuncAnimation(fig, update, \
        fargs = ('Animation, ', 1.8), \
        interval=100, frames=32, repeat=False)
