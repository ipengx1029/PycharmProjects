from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import mglearn

cancer = load_breast_cancer()
X_train,X_test,y_train,y_text = train_test_split(cancer.data,cancer.target,train_size=0.9,random_state=0)

n_neighbours_settings = range(1,10)
test_accuracy = []
train_accuracy= []
for i in n_neighbours_settings:
    clf = KNeighborsClassifier(n_neighbors=i)
    clf.fit(X_train,y_train)
    test_accuracy.append(clf.score(X_test,y_text))
    train_accuracy.append(clf.score(X_train,y_train))

plt.plot(n_neighbours_settings,train_accuracy)
plt.plot(n_neighbours_settings,test_accuracy)
plt.legend(labels=['train','test'])
plt.xlabel('neighbours')
plt.ylabel('accuracy')
# plt.show()

# mglearn.plots.plot_knn_regression(n_neighbors=1)
# plt.show()

