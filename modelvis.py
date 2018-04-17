"""
Visualising Machine Learning Models
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

__version__ = "0.1.2"
__author__ = "Amit Kapoor <amitkaps@gmail.com>" 

def plot_classifier_2d(clf, data, target, probability = False, alpha = 0.9):
    x_min, x_max = data.iloc[:,0].min(), data.iloc[:,0].max()
    y_min, y_max = data.iloc[:,1].min(), data.iloc[:,1].max()
    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, (x_max - x_min)/100), 
        np.arange(y_min, y_max, (y_max - y_min)/100))
    if probability == False:
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    else:
        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:,0]
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap="viridis", alpha = 0.5)
    plt.colorbar(cs)
    plt.scatter(x = data.iloc[:,0], y = data.iloc[:,1], c = target, s = 100, cmap="magma", alpha = alpha)

if __name__ == "__main__":
    print("welcome to model visualisation")