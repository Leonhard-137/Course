import numpy as np
import matplotlib.pyplot as plt

beta = np.linspace(0, 1, 5)
theta = np.linspace(0, np.pi, 100)

# 创建适当维度的 kappa 数组
kappa = np.zeros((len(beta), len(theta)))

# 计算每个 beta 对应的 kappa 曲线
for i, b in enumerate(beta):
    kappa[i, :] = (1 - b**2) / (1 + b * np.cos(theta))**2

# 绘图
plt.figure(figsize=(10, 6))

for i, b in enumerate(beta):
    plt.plot(theta, kappa[i], label=f'β = {b:.2f}')

plt.xlabel(r'$\theta$')
plt.ylabel(r'$\kappa = \frac{1-\beta^2}{(1+\beta\cos\theta)^2}$')
plt.legend()
plt.show()