from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

news = fetch_20newsgroups(subset='all')
x_train,x_test,y_train,y_test = train_test_split(news.data,news.target,test_size=0.3,random_state=0)
tf = TfidfVectorizer()
x_train = tf.fit_transform(x_train)
x_test = tf.transform(x_test)
mub = MultinomialNB()
mub.fit(x_train,y_train)
y_predict = mub.predict(x_test)
print(classification_report(y_test,y_predict,target_names=news.target_names))
print(y_predict)

# gc = GridSearchCV(mub,cv=3,param_grid={'alpha':[1,3,5]})
# gc.fit(x_train,y_train)
# print('交叉验证中最好测试结果：',gc.best_score_)
# print('最好参数模型：',gc.best_estimator_)
# print('每次后的训练集的准确率结果：',gc.cv_results_)