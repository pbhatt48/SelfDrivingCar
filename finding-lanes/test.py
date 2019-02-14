import numpy as np
import matplotlib.pyplot as plt


def draw(x1, x2):
    ln = plt.plot(x1, x2, 'ro-')


no_of_pts = 100
bias = np.ones(no_of_pts)
np.random.seed(0)
x1 = np.random.normal(10, 2, no_of_pts)
y1 = np.random.normal(12, 2, no_of_pts)
x2 = np.random.normal(5, 2, no_of_pts)
y2 = np.random.normal(6, 2, no_of_pts)
top_region = np.array([x1, y1, bias]).T
bottom_region = np.array([x2, y2, bias]).T
# plt.scatter(x1, y1, color='r', alpha=0.5)
# plt.scatter(x2, y2, color='b', alpha=0.5)
all_points = np.vstack((top_region, bottom_region))
# print(all_points)
w1 = -0.2
w2 = -.35
b = 3.5
line_parameters = np.matrix([w1, w2, b])
# print(line_parameters)
x1 = np.matrix([bottom_region[:, 0].min(), top_region[:, 0].max()])
x2 = -b / w2 + x1 * (-w1 / w2)
x1 = [-0.54518551, 14.53950925]
x2 = [10.31153458,  1.691709  ]
print(x1, x2)
_, ax = plt.subplots(figsize=(4, 4))
ax.scatter(top_region[:, 0], top_region[:, 1], color="r")
ax.scatter(bottom_region[:, 0], bottom_region[:, 1], color='b')
#draw(x1, x2)
plt.plot(x1, x2, 'ro-')
plt.show()
