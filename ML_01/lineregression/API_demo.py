from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

lb = load_boston()
#数据分割
x_train,x_test,y_train,y_test = train_test_split(lb.data,lb.target,test_size=0.2)
print('y-test1 :',y_test)
#进行标准化处理
std_x = StandardScaler()
x_train = std_x.fit_transform(x_train)
x_test = std_x.transform(x_test)
std_y = StandardScaler()
y_train = std_y.fit_transform(y_train.reshape(-1,1))
y_test = std_y.transform(y_test.reshape(-1,1))
print('y-test2:',y_test)
lr = LinearRegression()
lr.fit(x_train,y_train)
print(lr.coef_)
print(std_y.inverse_transform(lr.predict(x_test)))

# print("="*10+'岭回归里房子的预测价格归'+'='*10)
# rd = Ridge(alpha=1)
# rd.fit(x_train,y_train)
# print(rd.coef_)
# y_rd_predict = std_y.inverse_transform(rd.predict(x_test))
# print('岭回归里房子的预测价格：',y_rd_predict)
# print('岭回归的均方误差：',mean_squared_error(y_test,y_rd_predict))