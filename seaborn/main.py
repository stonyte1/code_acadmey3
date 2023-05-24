import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset('mpg')

# print(mpg)

grid = sns.FacetGrid(data=mpg, col='origin')
plot = grid.map(sns.scatterplot, 'acceleration', 'cylinders')

# correlation = mpg.corr(numeric_only=True)

# mozaik = sns.heatmap(correlation, annot=True)
# print(correlation)
# barplot = sns.barplot(x='cylinders', y=)


plt.show()