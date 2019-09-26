import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


class LinearRegression0:
    """具有通用性的多元线性回归的实现"""

    def __init__(self):
        self.coef_ = None       # 表示参数，theta_[1:]
        self.intercept_ = None   # 表示截距 ==>theta[0]
        self._thera = None       # 表示完整的theta==> theta[:]

    def fit_normal(self, x_train, y_train):
        """拟合"""
        # 构造数据集矩阵
        X_b = np.hstack([np.ones((len(x_train), 1)), x_train])
        # 计算系数
        self._thera = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
        self.coef_ = self._thera[1:]
        self.intercept_ = self._thera[0]
        return self

    def predict(self, x_test):
        X_b = np.hstack([np.ones((len(x_test), 1)), x_test])
        # X_b = np.hstack([np.ones(len(x_test), 1), x_test])
        # X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return np.array(X_b.dot(self._thera))

    def score(self, x_test, y_test):
        pass


if __name__ == "__main__":
    # 使用样例数据
    boston = datasets.load_boston()
    X = boston.data     # 特征数据集
    y = boston.target   # 目标变量

    plt.scatter(np.arange(len(y)), y, color="red")  # 有一些y顶在50的上限上
    X = X[y < 50]
    y = y[y < 50]

    from LinerRegression.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from LinerRegression.metrics import r2_score
    import LinerRegression

    X_train, x_test, y_train, y_test = train_test_split(X, y, seed=666)

    liner = LinearRegression()
    liner.fit(X_train, y_train)
    print("参数：", liner.coef_)
    print("偏置：", liner.intercept_)

    reg = LinearRegression0()
    reg.fit_normal(X_train, y_train)
    print("参数：", reg.coef_)
    print("偏置:", reg.intercept_)

    score = r2_score(y_test, liner.predict(x_test))
    score = liner.score(x_test, y_test)
    score2 = r2_score(y_test, reg.predict(x_test))
    print("score", score)            # 0.8129794056212811
    print("score2", score2)

    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import mean_absolute_error

    print(mean_squared_error(y_test, liner.predict(x_test)), LinerRegression.metrics.mean_squared_error(y_test, liner.predict(x_test)))
    print(mean_absolute_error(y_test, liner.predict(x_test)), LinerRegression.metrics.mean_absolute_error(y_test, liner.predict(x_test)))
    print(liner.score(x_test, y_test), LinerRegression.metrics.r2_score(y_test, liner.predict(x_test)))

