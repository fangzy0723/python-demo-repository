
# 对比ndarray 和 python列表的计算效率
import random
import time
import numpy as np

arr = []
for i in range(10000000):
    arr.append(random.random())

d1 = time.time()
sum1 = sum(arr)
d2 = time.time()

# 根据已有数组生成ndarray数组
arr2 = np.array(arr)
d3 = time.time()
sum2 = np.sum(arr2)
d4 = time.time()

print(d2-d1, d4-d3)
