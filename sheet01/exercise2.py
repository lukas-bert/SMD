import numpy as np
import matplotlib.pyplot as plt

#(a) the function should be unstable for all E and theta, because as theta approaches 0 this function is divided by a very small number leading to an numarical unstability

#input E in keV

def f(E,theta):
    return (2+(np.sin(theta))**2)/(1-(np.sqrt(1-(E/511)**(-2)))**2*(np.cos(theta))**2)

#(b)
#def fix(Theta):
   



x = np.linspace(-1*10**-7, 1*10**-7, 1000, dtype = "float64")

#print(f(50000,545))
plt.plot(x,f(50000,x))
plt.plot()
plt.show()
plt.close()