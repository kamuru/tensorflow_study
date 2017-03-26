
import tensorflow as tf
import numpy as np

num_points = 300
vectors_set = []
for i in range(num_points):
    x = np.random.normal(5, 5) + 15
    y = 1000 * x + 3000 + np.random.normal(0, 2000)
    vectors_set.append([x, y])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

cost = tf.reduce_sum(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.000005)
train = optimizer.minimize(cost)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

import matplotlib.pyplot as plt

for i in range(10000):
    sess.run(train)
    if i % 1000 == 0:
        print(sess.run(W), sess.run(b), sess.run(cost))

        plt.plot(x_data, y_data, 'ro')
        plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
        plt.xlim([0, 40])
        plt.ylim([0, 40000])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()