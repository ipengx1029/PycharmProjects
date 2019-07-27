from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

news = fetch_20newsgroups(subset='all')
x_train,x_test,y_train,y_test = train_test_split(news.data,news.target,test_size=0.1,random_state=0)
tf = TfidfVectorizer()
x_train = tf.fit_transform(x_train)
x_test = tf.transform(x_test)
knn = KNeighborsClassifier()
param = {"n_neighbors": [3, 5, 10]}
gc = GridSearchCV(knn,param_grid=param,cv=3)
gc.fit(x_train,y_train)
print('交叉验证中最好测试结果：',gc.best_score_)
print('最好参数模型：',gc.best_estimator_)
print('每次后的训练集的准确率结果：',gc.cv_results_)