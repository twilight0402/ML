import numpy as np
import matplotlib.pyplot as plt


class SimpleLinerRegression1:

    def __init(self):
        """待拟合的两个参数"""
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        """拟合函数，接收训练数据集。 计算a和b的值"""
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = 0.0   # 分子
        d = 0.0     # 分母

        for x, y in zip(x_train, y_train):
            num += (x - x_mean) * (y - y_mean)
            d += (x - x_mean) ** 2

        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

        return self

    def predict(self, x_predict):
        """对输入的x，预测所对应的所有y"""
        assert x_predict.ndim == 1, \
            "Simple Linear Regressor can only solve single feature training data."
        assert self.a_ is not None and self.b_ is not None, \
            "must fit before predict!"

        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x_single):
        """只对单个数据进行预测"""
        return self.a_ * x_single + self.b_

    def __repr__(self):
        return "SimpleLinearRegression1()"


class SimpleLinerRegression:
    """改进的线性回归"""

    def __init(self):
        """待拟合的两个参数"""
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        """拟合函数，接收训练数据集。 计算a和b的值"""
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        # ndarry的内积运算
        num = (x_train - x_mean).dot(y_train - y_mean)
        d = (x_train - x_mean).dot(x_train - x_mean)

        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

        return self

    def predict(self, x_predict):
        """对输入的x，预测所对应的所有y"""
        assert x_predict.ndim == 1, \
            "Simple Linear Regressor can only solve single feature training data."
        assert self.a_ is not None and self.b_ is not None, \
            "must fit before predict!"

        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x_single):
        """只对单个数据进行预测"""
        return self.a_ * x_single + self.b_

    def __repr__(self):
        return "SimpleLinearRegression1()"


if __name__ == "__main__":
    spl = SimpleLinerRegression()
    x = np.array([1,2,3,4,5])
    y = np.array([1,3,2,3,5])
    spl.fit(x, y)       # 进行拟合

    print("a:", spl.a_)
    print("b:", spl.b_)

    y_hat = spl.predict(x)  # 预测的分割线

    plt.scatter(x, y)
    plt.plot(x, y_hat, color="red")
    plt.axis([0, 6, 0, 6])
    plt.show()
