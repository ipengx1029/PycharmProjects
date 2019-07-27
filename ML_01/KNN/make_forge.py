import mglearn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# X,y=mglearn.datasets.make_forge()
# mglearn.discrete_scatter(X[:,0],X[:,1],y)
# plt.legend(['Class 0','Class 1'])
# plt.show()


X,y=mglearn.datasets.make_wave(n_samples=40)
plt.scatter(X,y)
plt.axis([-3,3,-5,5])
plt.show()