import jieba
from sklearn.feature_extraction.text import CountVectorizer

c = jieba.cut('每个文档中的词，只是整个语料库中所有词，的很小的一部分，这样造成特征向量的稀疏矩阵为了解决存储和运算速度的问题')
a=list(c)
b = ' '.join(a)
vect = CountVectorizer()
x=vect.fit_transform([b])
print(x.toarray())



