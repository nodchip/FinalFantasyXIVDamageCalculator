import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return ((t - 1.0) / 99.0) ** 7.0

t1 = np.arange(1.0, 99.0, 1.0)

plt.figure(figsize=(12, 9))
plt.grid()
plt.bar(t1, f(t1))
plt.savefig('figure.png')
