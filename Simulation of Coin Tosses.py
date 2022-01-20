import matplotlib.pyplot as plt
import numpy as np

y = np.random.randint(0, 2, 100000)

heads = np.count_nonzero(y == 0)

tails = np.count_nonzero(y == 1)

toss = {'heads': heads, 'tails': tails}
print(toss)
courses = list(toss.keys())
values = list(toss.values())

print(courses)
print(values)

plt.bar(courses, values)

plt.xlabel("Heads or Tails")
plt.ylabel("Count of Tosses")
plt.title("Simulation of Coin Tosses")
plt.show()
