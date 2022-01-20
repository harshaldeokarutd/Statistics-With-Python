import numpy as np
import matplotlib.pyplot as mp
x2 = np.array([])
for i in range(100000):
    x1 = np.random.randint(1, 6, 10)
    x2 = np.concatenate((x2, np.average(x1)), axis=None)


mp.hist(x2)
mp.show()
