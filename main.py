from data import main_data
import matplotlib as mb
import matplotlib.pyplot as plt
import numpy as np

N = 50
x = []
y = []
for z in main_data:
    x.append(main_data[z]["price"])
    y.append(main_data[z]["speed"])

colors = np.random.rand(N)


plt.scatter(x, y, c=colors)
plt.show()