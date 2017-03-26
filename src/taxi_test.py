import numpy as np
import matplotlib.pyplot as plt

num_points = 300
vectors_set = []
for i in range(num_points):
    x = np.random.normal(5, 5) + 15
    y = x * 1000 + 3000 + np.random.normal(0, 2000)
    vectors_set.append([x, y])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

# df = pd.DataFrame({'x':x_data, 'y':y_data})
# sns.lmplot('x', 'y', data=df, fit_reg=False, size=6)
#
# dd = pd.DataFrame({'x':x_data, 'y':x_data * 1000 + 3000})
# sns.lmplot('x', 'y', data=dd, fit_reg=False, size=6)

plt.plot(x_data,y_data,'ro')
x = np.arange(0, 35)
# plt.plot(x * 1000 + 3000)

plt.xlim([0,35])
plt.ylim([0,40000])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()

