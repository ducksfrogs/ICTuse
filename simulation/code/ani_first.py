import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

ingBuffer = []
mark_list = ["4", "8", "p", "*", "x", "D", "4", "8", "p", "x"]
loop = len(mark_list)
num = 8

for i in range(loop):
    x = np.random.randn(num)
    y = np.random.randn(num)
    img = plt.plot(x, y, linewidth=0, marker=mark_list[i], markersize=15)
    ingBuffer.append(img)
    ts = 300
    ani = animation.ArtistAnimation(fig, ingBuffer, interval=ts, repeat=False)

# FuncAnimation sample

fig = plt.figure(figsize=(6, 2))
x = np.arange(0, 10, 0.01)

def update(k, fig_name, Amp):
    plt.cla()
    y = Amp+np.sin(x-k)
    plt.plot(x, y, 'r')
    plt.xlim(-1.2*Amp, 1.2*Amp)
    plt.title(fig_name + 'Frame k=' + str(k))

ani = animation.FuncAnimation(fig, update, fargs=('Animation', 1.8), interval=100, frames=32, repeat=False)
