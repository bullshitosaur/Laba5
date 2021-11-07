import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1234)

sigma = 24
x = sigma + np.random.randn(1234)

ax = plt.subplot()

num_bins = 50
n, bins, patches, = ax.hist(x, num_bins, density=True)

ax.set(xlabel="t°C", title="average temperature in july")

plt.show()