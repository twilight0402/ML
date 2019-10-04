import numpy as np
import matplotlib.pyplot as plt
# from LinerRegression.model_selection import train_test_split


class aDebugGradient:
    """随机梯度下降法"""

    def __init__(self):
        self.coef_ = None       # 表示参数，theta_[1:]
        self.intercept_ = None  # 表示截距 ==>theta[0]
        self._thera = None      # 表示完整的theta==> theta[:]

    def fit_debug(self, X_train, y_train, eta=0.01, n_iters=1e4):
        """使用梯度下降法寻找最小的代价函数"""
        # 格式化X和theta，加上x0 和 theta0
        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])

        # 调用循环的梯度下降
        self._thera = self.gradient_Descent(self.dj_debug, X_b, y_train, initial_theta, eta, n_iters)
        self.intercept_ = self._thera[0]
        self.coef_ = self._thera[1:]
        return self

    def J(self, theta, X_b, y):
        return np.sum((y - X_b.dot(theta)) ** 2) / len(y)

    def dj_debug(self, X_b, theta, y, epsilon=0.001):
        res = np.zeros((len(theta), ))
        for i in range(len(theta)):
            theta_1 = theta.copy()
            theta_2 = theta.copy()
            theta_1[i] += epsilon
            theta_2[i] -= epsilon
            res[i] = (self.J(theta_1, X_b, y) - self.J(theta_2, X_b, y)) / (2 * epsilon)
        return res

    def dJ_math(self, X_b, theta, y):
        return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(y)

    def gradient_Descent(self, dj, X_b, y_train, initial_theta, eta, n_iters,  epsilon=1e-8):
        """梯度下降"""
        theta = initial_theta
        for i in range(int(n_iters)):
            gradient = dj(X_b, theta, y_train)      # 计算得到梯度
            last_theta = theta
            theta = theta - eta * gradient
            if np.absolute(self.J(theta, X_b, y_train) - self.J(last_theta, X_b, y_train)) < epsilon:
                break
        return theta

    def predict(self, x_test):
        X_b = np.hstack([np.ones((len(x_test), 1)), x_test])
        return np.array(X_b.dot(self._thera))

    def score(self, X_test, y_test):
        from LinerRegression import metrics
        y_test_predict = self.predict(X_test)
        return metrics.r2_score(y_test, y_test_predict)


if __name__ == "__main__":
    from sklearn import datasets
    data = datasets.load_boston()
    X = data.data
    y = data.target

    # 剔除噪音
    X = X[y < 50]
    y = y[y < 50]

    m = 100000
    x = np.random.normal(size=m)        # (n,)一维向量 [1,2,3,4,5]
    X = x.reshape(-1, 1)                # 二维向量 (n,1)表示n行，1列 [[1],[2]]
    y = 4. * x + 3. + np.random.normal(0, 3, size=m)

    # 数据归一化处理
    from sklearn.preprocessing import StandardScaler

    # standardScaler = StandardScaler()
    # standardScaler.fit(X)
    # X_standard = standardScaler.transform(X)

    # 交叉验证
    # X_train_standard, X_test_standard, y_train, y_test = train_test_split(X_standard, y, test_ratio=0.2, seed=666)

    sgd = aDebugGradient()
    sgd.fit_debug(X, y)
    print(sgd.intercept_, " ,", sgd.coef_)
