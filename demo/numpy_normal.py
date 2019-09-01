# 正态分布
import numpy as np
import matplotlib.pyplot as plt

data1 = np.random.normal(loc=2, scale=0.1, size=1000000)
# 1、创建画布
plt.figure(figsize=(20, 8), dpi=8)
# 2、绘制直方图 所有数据分1000组
plt.hist(data1, 1000)
# 3、显示画布
plt.show()