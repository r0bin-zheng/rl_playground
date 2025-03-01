import numpy as np
import matplotlib.pyplot as plt
import time

# 初始化二维数据
data = np.random.rand(10, 10)

# 创建一个图形和一个子图
fig, ax = plt.subplots()

# 创建一个图像对象
im = ax.imshow(data, cmap='viridis')

# 显示图形
plt.ion()  # 打开交互模式
plt.show()

# 主循环
for _ in range(100):  # 假设我们循环100次
    # 更新数据，这里我们随机生成新的数据
    data = np.random.rand(10, 10)
    # 更新图像对象的数据
    im.set_array(data)
    # 刷新图形
    plt.draw()
    plt.pause(0.1)  # 暂停0.1秒以便图形有时间更新

# 关闭交互模式
plt.ioff()
plt.show()