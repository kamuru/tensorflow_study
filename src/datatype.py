# import tensorflow as tf
#
# a = tf.constant([10], tf.float32)
# b = tf.constant([1, 2, 3])
# c = tf.constant([[5, 2, 0], [6, 8, 9]], tf.float32)
#
# print(a)
# print(b)
# print(c)
#
#
#
# # v = tf.Variable(5, name='v3')
#
#
# sess = tf.Session()
# file_writer = tf.summary.FileWriter('tensorboardlog', sess.graph)
#
# sess.run(tf.global_variables_initializer())

# import tensorflow as tf
#
# a = tf.placeholder(dtype=tf.int32)
# b = tf.placeholder(dtype=tf.int32)
# c = tf.placeholder(dtype=tf.int32)
# d = a * b + c
#
# input_a = [1, 3, 5, 7, 9]
# input_b = [2, 4, 6, 8, 0]
# input_c = [1, 2, 3, 4, 5]
#
# sess = tf.Session()
# result = sess.run(d, feed_dict={a:input_a, b:input_b, c:input_c})
#
# print(result)

import tensorflow as tf

W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
