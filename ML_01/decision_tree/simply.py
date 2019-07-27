import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def decision():
    data = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    print(type(data))
    x=data[['pclass','age','sex']]
    x['age'].fillna(x['age'].mean(),inplace=True)
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)
    dict = DictVectorizer()
    x_train = dict.fit_transform(x_train.to_dict(orient='records'))
    x_test = dict.fit_transform(x_test.to_dict(orient='records'))
    # dtc = DecisionTreeClassifier()
    # dtc.fit(x_train,y_train)
    # y_precidt=dtc.predict(x_test)
    # print(y_precidt)
    # print(np.mean(y_test==y_precidt))
    # print(dtc.score(x_test,y_test))

    rfc = RandomForestClassifier()
    parser = {'n_estimators':[100,200,300,400,500],'max_depth':[3,6,9,12,16]}
    gc = GridSearchCV(estimator=rfc,param_grid=parser,cv=2)
    gc.fit(x_train,y_train)
    print('准确率为：',gc.score(x_test,y_test))
    print('交叉验证中最好测试结果：', gc.best_score_)
    print('最好参数模型：', gc.best_estimator_)
    print('每次后的训练集的准确率结果：', gc.cv_results_)
if __name__ == '__main__':
    decision()