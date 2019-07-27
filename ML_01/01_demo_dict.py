from sklearn.feature_extraction import DictVectorizer
dict = DictVectorizer()
text = [{'xupeng':'111'},{'wansiying':'222'}]
x = dict.fit_transform(text)
print(x.toarray())