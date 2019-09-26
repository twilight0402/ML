import numpy as np
from math import sqrt


def mean_squared_error(y_true, y_predict):
    """均方误差"""
    return np.sum((y_predict-y_true)**2) / len(y_true)


def root_mean_squared_error(y_true, y_predict):
    """均方根误差"""
    return sqrt(mean_squared_error(y_true, y_predict))


def mean_absolute_error(y_true, y_predict):
    """平均绝对误差"""
    return np.sum(np.absolute(y_true - y_predict)) / len(y_true)


def r2_score(y_true, y_predict):
    """R方"""
    return 1 - mean_squared_error(y_true, y_predict) / np.var(y_true)