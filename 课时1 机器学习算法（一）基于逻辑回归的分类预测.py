import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression

x_features = np.array(
    [
        [-1, -2],
        [-2, -1],
        [-3, -2],
        [1, 3],
        [2, 1],
        [3, 2]
    ]
)
y_label = np.array([0, 0, 0, 1, 1, 1])
lr_clf = LogisticRegression()
lr_clf = lr_clf.fit(x_features, y_label)
print(lr_clf)
## 查看其对应模型的w
print('the weight of Logistic Regression:', lr_clf.coef_)

## 查看其对应模型的w0
print('the intercept(w0) of Logistic Regression:', lr_clf.intercept_)
plt.figure()
plt.scatter(x_features[:, 0], x_features[:, 1], c=y_label, s=50, cmap='viridis')
plt.show()

## 可视化决策边界
plt.figure()
plt.scatter(x_features[:, 0], x_features[:, 1],
            c=y_label, s=50, cmap='viridis')

plt.title('Dataset')
nx, ny = 200, 100
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
x_grid, y_grid = np.meshgrid(np.linspace(x_min, x_max, nx), np.linspace(y_min, y_max, ny))
z_proba = lr_clf.predict_proba(np.c_[x_grid.ravel(), y_grid.ravel()])
