import numpy as np
import matplotlib.pyplot as plt
from LinerRegression.model_selection import train_test_split


class StochasticDescent:
    """随机梯度下降法"""

    def __init__(self):
        self.coef_ = None       # 表示参数，theta_[1:]
        self.intercept_ = None  # 表示截距 ==>theta[0]
        self._thera = None      # 表示完整的theta==> theta[:]

    def fit_SGD(self, X_train, y_train, eta=0.01, n_iters=1):
        """使用梯度下降法寻找最小的代价函数"""
        # 格式化X和theta，加上x0 和 theta0
        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])

        # 调用循环的梯度下降
        self._thera = self.sgd(X_b, y_train, initial_theta, n_iters, 5, 50)  # , eta=eta, n_iters=n_iters)
        self.intercept_ = self._thera[0]
        self.coef_ = self._thera[1:]
        return self

    def sgd(self, X_b, y_train, initial_theta, n_iters, t0=5, t1=50):
        """随机梯度下降, niters是轮数"""

        def get_study_rate(i_iters):
            """把学习率和迭代次数联系起来"""
            return t0 / (t1 + i_iters)

        def dJ_sgd(X_b_i, theta, y):
            """计算随机一个元素的梯度"""
            return 2 * X_b_i.T.dot(X_b_i.dot(theta) - y)

        m = len(X_b)
        theta = initial_theta
        for n in range(int(n_iters)):
            indexes = np.random.permutation(m)
            X_b_new = X_b[indexes, :]
            y_new = y[indexes]
            for i in range(m):
                sgd = dJ_sgd(X_b_new[i], theta, y_new[i])
                theta = theta - get_study_rate(m * n + i) * sgd
        return theta

    def predict(self, x_test):
        X_b = np.hstack([np.ones((len(x_test), 1)), x_test])
        return np.array(X_b.dot(self._thera))

    def score(self, X_test, y_test):
        from LinerRegression import metrics
        y_test_predict = self.predict(X_test)
        return metrics.r2_score(y_test, y_test_predict)


if __name__ == "__main__" :

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

    sgd = StochasticDescent()
#    sgd.fit_SGD(X, y, n_iters=5)
    print(sgd._thera)

    from sklearn.linear_model import SGDRegressor

    sgd_reg = SGDRegressor(max_iter=50)
    sgd_reg.fit(X, y)
    print(sgd_reg.coef_, sgd_reg.intercept_)