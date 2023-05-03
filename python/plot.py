import numpy as np
from matplotlib import pyplot as p

x = np.array([1, 2, 3])
y = np.array([2, 3, 4])

xx, yy = np.meshgrid(x, y)
p.plot(xx, yy, marker = '.', linestyle = 'none', color = 'r')
p.show()