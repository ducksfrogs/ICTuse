import vpython as vp
import numpy as np

b = vp.box()

b.color = vp.vector(1, 1, 0)
b.size = vp.vector(1, 2, 5)
b.pos = vp.vector(2, 0, -5)

scene = vp.canvas(width=600, height=600, title='cube-Spring')
cube = vp.box(size=vp.vector(cube_size, cube_size, cube_size), color=vp.color.orange)
floor 
