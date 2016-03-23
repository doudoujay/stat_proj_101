from data import main_data
import time
import matplotlib as mb
import matplotlib.pyplot as plt
from numpy import *
from regression import *
import pylab as lab
import matplotlib.mlab as mlab
import math
import scipy.stats as stats

N = 100000
x = []
y = []


# load data
print "step 1: load data"
for z in main_data:
    each = main_data[z]
    x.append(each["price"])
    y.append(each["quality"])

colors = random.rand(N)
y_sort = sorted(y)
# calculate linear regression
(m, b) = lab.polyfit(x, y, 1)

yp = polyval([m, b], x)

# draw graph


fig = plt.figure(figsize=(8,8))

ax1 = fig.add_subplot(221)
ax1.set_xlabel('Price')
ax1.set_ylabel('Quality')
ax1.set_title("Random scatterplot")
plt.plot(x,yp)
plt.scatter(x,y)

# hist and normal

ax2 = fig.add_subplot(222)


plt.hist(y, bins=100)
ax2.set_xlabel('quality value')
ax2.set_ylabel('cumulative sum')
ax2.set_title("Normal distrubution")



ax3 = fig.add_subplot(223)
ax3.set_title("normal")
hmean = mean(y_sort)
hstd = std(y_sort)
pdf = stats.norm.pdf(y_sort, hmean, hstd)
plt.plot(y_sort, pdf)
print(hmean, hstd)


ax4 = fig.add_subplot(224)
ax4.set_title('residual plot')
#Residual plot
difference = yp-y
plt.scatter(x,difference)

plt.grid()


plt.show()