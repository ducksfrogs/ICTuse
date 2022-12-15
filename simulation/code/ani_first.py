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
