import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('./mnist/input_data', one_hot=True)

sess = tf.Session()
sess.run(mnist)

print('a')