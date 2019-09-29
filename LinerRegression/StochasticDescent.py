import numpy as np
import matplotlib.pyplot as plt
from LinerRegression.model_selection import train_test_split


class StochasticDescent:
    """随机梯度下降法"""

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


if __name__ == "__main__" :
    pass