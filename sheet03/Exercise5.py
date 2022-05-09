import numpy as np
from project_a1.random import LCG
import matplotlib.pyplot as plt

# Task b)

def check_array (value, array):
    for i in range(len(array)):
        if array[i] == value:
            return False
    return True        

def periodtest(a1):
    seed1 = 0
    i = 0
    gen = LCG(seed = seed1, a = a1, c = 3, m = 1024)
    x = np.zeros(1024)
    gen.advance()
    while i <= 1024 and (gen.state != seed1) and check_array(gen.state, x):
        x[i] = gen.state
        gen.advance()
        i =  i + 1
    return i    

print(periodtest(10))
print(periodtest(1))
print(periodtest(69))
print(periodtest(5))
print(periodtest(3))
print(periodtest(4))

# Tasks d) - f)

# Numpy generator
rng = np.random.default_rng(420)
x, y, z = rng.uniform(size = (3, 10000))

# Our LCG
gen = LCG(seed = 0, a = 1601, c = 3456, m = 10000)          # Exercise Parameters
x2, y2, z2 = gen.uniform(size = (3, 10000))

good_gen = LCG(seed = 0, a = 625, c = 6571, m = 31104)      # Good Parameters
x3, y3, z3 = good_gen.uniform(size = (3, 10000))

# Dependency on start value

values = [0, 69, 420, 187, 1337, 31415926, 999, 15376452, 41251]
fig0 = plt.figure()

for i in range(len(values)):
    ax = fig0.add_subplot(3, 3, i+1)
    tempgen = LCG(seed = values[i], a = 1601, c = 3456, m = 10000)
    ax.hist(tempgen.uniform(size = 10000), bins = 100)
    ax.set_title(f"Seed = {values[i]}")

fig0.tight_layout()
plt.show()

# Comparison of our LCG vs numpy.random

fig = plt.figure()

ax1 = fig.add_subplot(2, 3, 1)
ax1.hist(y2, bins = 100)            # Histogram of our "random" numbers
ax1.set_title("LCG")

ax2 = fig.add_subplot(2, 3, 4)
ax2.scatter(
    x2, y2,
    s=5,
    #smaller points
    alpha=0.3,
    # 70% transparency
)

ax3 = fig.add_subplot(2, 3, 2)
ax3.hist(y, bins = 100)             # histogram of numpy's random numbers
ax3.set_title("numpy.random")

ax4 = fig.add_subplot(2, 3, 5)
ax4.scatter(
    x, y,
    s=5,
    #smaller points
    alpha=0.3,
    #70% transparency
)

ax5 = fig.add_subplot(2, 3, 3)
ax5.hist(y3, bins = 100)             # histogram of numpy's random numbers
ax5.set_title("LCG w/ good params")

ax6 = fig.add_subplot(2, 3, 6)
ax6.scatter(
    x3, y3,
    s=5,
    #smaller points
    alpha=0.3,
    #70% transparency
)

fig.tight_layout()


# 3D Scatter-Plots

plt.show()

fig2 = plt.figure()

ax = fig2.add_subplot(1, 3, 1, projection='3d')

ax.scatter(
    x2, y2, z2,
    s=5,
    # smaller points
    alpha=0.3,
    # 70% transparency
)
ax.set_title("LCG")
# set the orientation of the 3d axis

ax.view_init(elev=30, azim=20)

ax2 = fig2.add_subplot(1, 3, 2, projection='3d')

ax2.scatter(
    x, y, z,
    s=5,
    # smaller points
    alpha=0.3,
    # 70% transparency
)
ax2.set_title("numpy.random")

# set the orientation of the 3d axis

ax2.view_init(elev=30, azim=20)

ax3 = fig2.add_subplot(1, 3, 3, projection='3d')

ax3.scatter(
    x3, y3, z3,
    s=5,
    # smaller points
    alpha=0.3,
    # 70% transparency
)
ax3.set_title("LCG w/ good params")
# set the orientation of the 3d axis

ax.view_init(elev=30, azim=20)

plt.show()
