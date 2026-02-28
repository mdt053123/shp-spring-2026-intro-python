from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
import pandas as pd

# 1-NN Classification
data = pd.DataFrame({'x': [0, 5, 10], 'y': [0, 5, 0], 'color' : ['red', 'blue', 'green']})
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data[['x', 'y']], data['color'])
print(knn.predict([[3, 2]]))