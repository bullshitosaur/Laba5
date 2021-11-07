import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.01)
y = np.arccos(x**2)**np.e**x

ax = plt.subplot()
ax.plot(x, y)

ax.set(xlabel="x", ylabel="y", title="y = arccos(x²)^e^x")
plt.grid()

plt.show()