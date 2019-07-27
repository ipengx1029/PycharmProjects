from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import mglearn
import numpy as np

iris_dataset = load_iris()
x_train,x_test,y_train,y_test = train_test_split(iris_dataset.data,iris_dataset.target,test_size=0.2,random_state=0)
# iris_dataframe = pd.DataFrame(x_train,columns=iris_dataset.feature_names)
# grr =pd.plotting.scatter_matrix(iris_dataframe,c=y_train,figsize=(15,15),marker='o',hist_kwds={'bins':20},s=60,alpha=.8,cmap=mglearn.cm3)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
# x_new=np.array([[1,1,1,9]])
# prediction  =knn.predict(x_new)
# print(prediction)

y_pred = knn.predict(x_test)
print(np.mean(y_pred==y_test))

print(knn.score(x_test,y_test))