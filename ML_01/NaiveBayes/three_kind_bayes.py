import numpy as np

#高斯朴素贝叶斯
def GaussianNB1():
    X = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
    Y = np.array([1,1,1,2,2,2])
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(X,Y)
    print(clf.predict([[-0.8, -1]]))

def MultinomialNB1():
    X_train = np.random.randint(5,size=(6,100))
    Y_train = np.array([1,2,3,4,5,6])
    from sklearn.naive_bayes import MultinomialNB
    mul = MultinomialNB(alpha=3)
    mul.fit(X_train,Y_train)
    print(mul.predict(np.random.randint(5,size=(1,100))))

# 伯努利朴素贝叶斯
def BernoulliNB1():
    X = np.random.randint(2,size=(6,100))
    Y = np.array([1,2,3,4,5,6])
    from sklearn.naive_bayes import BernoulliNB
    bll = BernoulliNB()
    bll.fit(X,Y)
    print(bll.predict(X[2:3]))

if __name__ == '__main__':
    # GaussianNB1()
    # MultinomialNB1()
    BernoulliNB1()