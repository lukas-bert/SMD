import numpy as np
import matplotlib.pyplot as plt

#deviation by more than 1 percent
def f(x):
    return (x**3+(1/3))-(x**3-(1/3))

for x in range(48988):
    if((np.abs(f(x)-(2/3))/(2/3)) > 0.01):
        print("f(x) deviates by more than 1 percent for all x >", x)
        break

for x in range(48988):
    if((np.abs(f(-x)-(2/3))/(2/3)) > 0.01):
        print("f(x) deviates by more than 1 percent for all x <", -x)
        break

def g(x):
    return ((3+((x**3)/3))-(3-((x**3)/3)))/x**3
n = 100000000000

for x in range(1,n):
    if((np.abs(g(1/x)-(2/3))/(2/3)) > 0.01):
        print("g(x) deviates by more than 1 percent for all x <", 1/x)
        break

for x in range(1,n):
    if((np.abs(g(-1/x)-(2/3))/(2/3)) > 0.01):
        print("g(x) deviates by more than 1  percent for all x >",-1/x)
        break

#equal to zero

for x in range(10000000):
    if(f(x) == 0):
        print("f(x) is equal to 0 for all x >", x)
        break

for x in range(10000000):
    if(f(-x) == 0):
        print("f(x) is equal to 0 for all x <", -x)
        break

for x in range(1,n):
    if(g(1/x) == 0):
        print("g(x) is equal to 0 for 0 < x <", 1/x)
        break

for x in range(1,n):
    if(g(-1/x) == 0):
        print("g(x) is equal to 0 for 0 > x >", -1/x)
        break

#graphic representaion c

#f(x)
y = np.linspace(-200000,200000,1000000)
plt.plot(y, f(y))
plt.plot(y, 0*y + 2/3)
plt.show()
plt.close()

#g(x)

x = np.linspace(-0.0001,0.0001,10000)
plt.plot(x, g(x))
plt.plot(x, 0*x + 2/3)
plt.show()
plt.close()

#d datatypes
y32 = np.linspace(-100,100,10000, dtype="float32")
y64 = np.linspace(-200000,200000,1000000, dtype="float64")
plt.plot(y, f(y), label = "normal")
plt.plot(y64, f(y64), label = "float64", linestyle = "dotted")
plt.legend()
plt.show()
plt.close()

plt.plot(y32, f(y32), label = "float32")
plt.legend()
plt.show()
plt.close()

x = np.linspace(-0.0001,0.0001,10000)
x32 = np.linspace(-0.1,0.1,10000, dtype="float32")
x64 = np.linspace(-0.0001,0.0001,10000, dtype="float64")
plt.plot(x, g(x), label = "normal")

plt.plot(x64, g(x64), label = "float64")
plt.legend()
plt.show()
plt.close()

plt.plot(x32, g(x32), label = "float32")
plt.legend()
plt.show()
plt.close()
