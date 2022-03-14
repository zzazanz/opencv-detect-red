import numpy as np
import matplotlib.pyplot as plt

normal_random = np.random.normal(0, 50, 100)

plt.hist(normal_random)
plt.show()