import numpy as np
from project_a1.random import LCG
import matplotlib.pyplot as plt

# d)
rng = np.random.default_rng(420)

x, y, z = rng.uniform(size = (3, 10000))


gen = LCG(seed = 0, a = 1601, c = 3456, m = 10000000)
#gen.__init__("gen", seed = 0, a = 1601, c = 3456, m = 10000)
x2, y2, z2 = gen.uniform(size = (3, 10000))

plt.hist(y2, bins = 100)

plt.show()

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

ax.scatter(
    x2, y2,
    s=5,
    # smaller points
    #alpha=0.3,
    ## 70% transparency
)

# set the orientation of the 3d axis

plt.show()

# e)

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.scatter(
    x2, y2, z2,
    s=5,
    # smaller points
    alpha=0.3,
    # 70% transparency
)

# set the orientation of the 3d axis

ax.view_init(elev=30, azim=20)

plt.show()
