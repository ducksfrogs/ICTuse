import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3)
y1 = x
y2 = x ** 2
y3 = x ** 3
y4 = x ** 4

fig = plt.subplots(figsize=(10, 3))
plt.plot(x, y2, c='k', label='y2')
plt.plot(x, y3, c='r', label='y3')

plt.xlabel('x')
plt.ylabel('y')
plt.title('example')
plt.grid()
plt.legend(loc='upper left')

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
axs[0,0].plot(x, y1, label='y1')
axs[0,1].plot(x, y2, label='y2')
