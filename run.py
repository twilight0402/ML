import numpy as np

x = np.array([[1,3,5], [2,4,6]])
print(x)
print()
print(np.cov(x, rowvar=0))

mean = np.mean(x, axis=1)
print(mean)

#减去均值
meanVals = np.mean(x,axis = 0)
dataMean = x - meanVals
#求协方差方阵
conMat = x.T.dot(dataMean)

print(meanVals)
print(dataMean)
print(conMat)

a = np.linspace(1,10,10)
print(a[:-1000])