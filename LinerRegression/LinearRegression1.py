import numpy as np
import matplotlib.pyplot as plt
from LinerRegression.model_selection import train_test_split


class LinearRegression1:
    def __init__(self):
        self.coef_ = None       # 表示参数，theta_[1:]
        self.intercept_ = None   # 表示截距 ==>theta[0]
        self._thera = None       # 表示完整的theta==> theta[:]

    def J(self, theta, X_b, y):
        try:
            return np.sum((y - X_b.dot(theta)) ** 2) / len(y)
        except:
            return float('inf')

    def dJ(self, theta, X_b, y):
        res = np.empty(len(theta))                      ##### zeros(5) == zeros((5,)) != zeros((5,1))
        res[0] = np.sum(X_b.dot(theta) - y)             # 需要将向量求和。没有办法，这里只能手动分开求解。因为这里X是从列方向分割，没有X0
        for i in range(1, len(theta)):
            res[i] = (X_b.dot(theta) - y).dot(X_b[:, i])
        return res * 2 / len(X_b)

    def gradient_descent(self, X_b, y, initial_theta, eta, n_iters=1e4, epsilon=1e-8):
        theta = initial_theta
        cur_iter = 0

        while cur_iter < n_iters:
            gradient = self.dJ(theta, X_b, y)
            last_theta = theta
            theta = theta - eta * gradient
            if np.absolute(self.J(theta, X_b, y) - self.J(last_theta, X_b, y)) < epsilon:
                break
            cur_iter += 1

        return theta

    def fit_gd(self, X_train, y_train, eta=0.01, n_iters=1e4):
        """使用梯度下降法寻找最小的代价函数"""
        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])
        self._theta = self.gradient_descent(X_b, y_train, initial_theta, eta, n_iters)

        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]


class LinearRegression2:
    def __init__(self):
        self.coef_ = None       # 表示参数，theta_[1:]
        self.intercept_ = None  # 表示截距 ==>theta[0]
        self._thera = None      # 表示完整的theta==> theta[:]

    def fit_gd(self, X_train, y_train, eta=0.01, n_iters=1e4):
        """使用梯度下降法寻找最小的代价函数"""
        # 格式化X和theta，加上x0 和 theta0
        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])

        # 调用循环的梯度下降
        self._thera = self.gradient_descent(X_b, y_train, initial_theta, eta=eta, n_iters=n_iters)
        self.intercept_ = self._thera[0]
        self.coef_ = self._thera[1:]
        return self

    def gradient_descent(self, X_b, y, initial_theta, eta, n_iters=1e4, epsilon=1e-8):
        theta = initial_theta

        i = 0
        while i < n_iters:
            i += 1
            lastTheta = theta  # 记录上一个参数向量
            dj = self.dj(theta, X_b, y)
            theta = theta - eta * dj
            if np.absolute(self.J(lastTheta, X_b, y) - self.J(theta, X_b, y)) < epsilon:
                break
        return theta

    def dj(self, theta, X_b, y):
        """计算代价函数的偏导数"""
        return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(y)

    def J(self, theta, X_b, y):
        """计算代价函数"""
        return np.sum((y - X_b.dot(theta)) ** 2) / len(y)

    def predict(self, x_test):
        X_b = np.hstack([np.ones((len(x_test), 1)), x_test])
        return np.array(X_b.dot(self._thera))

    def score(self, X_test, y_test):
        from LinerRegression import metrics
        y_test_predict = self.predict(X_test)
        return metrics.r2_score(y_test, y_test_predict)

if __name__ == "__main__":
    # np.random.seed(666)
    # x = 2 * np.random.random(size=100)
    # y = x * 3. + 4. + np.random.normal(size=100)
    # X = x.reshape(-1, 1)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_ratio=0.2, seed=666)
    #
    # line = LinearRegression2()
    # line.fit_gd(X_train, y_train)
    #
    # print(line.intercept_)
    # print(line.coef_)

    from sklearn import datasets
    X = datasets.load_boston().data
    y = datasets.load_boston().target

    # 剔除噪音
    X = X[y < 50]
    y = y[y < 50]

    # 数据归一化处理
    from sklearn.preprocessing import StandardScaler

    standardScaler = StandardScaler()
    standardScaler.fit(X)
    X_standard = standardScaler.transform(X)

    # 交叉验证
    X_train_standard, X_test_standard, y_train, y_test = train_test_split(X_standard, y, test_ratio=0.2, seed=666)

    linear = LinearRegression2()
    linear.fit_gd(X_train_standard, y_train, n_iters=3e5)
    print(linear.score(X_test_standard, y_test))

    from sklearn.linear_model import LinearRegression
    linear2 = LinearRegression()
    linear2.fit(X_train_standard, y_train)
    print(linear2.score(X_test_standard, y_test))

    print(linear.coef_)
    print(linear2.coef_)