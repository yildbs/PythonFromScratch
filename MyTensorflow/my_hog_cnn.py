import read_image_to_batch
import tensorflow as tf
import math
from scipy import misc
import glob
import matplotlib.pyplot as plt
import numpy as np
import cv2
from random import shuffle

train_data = read_image_to_batch.MyData()
train_data.set_num_label(2)
#Add train image to train_data
#positive image
list_train_data = [[path, 1] for path in glob.glob("../train_pos/*")]
#negative image
list_train_data.extend([[path, 0] for path in glob.glob("../train_neg_cropped/*")])
shuffle(list_train_data)

keys = [l[0] for l in list_train_data]
values = [l[1] for l in list_train_data]

train_data.add_image_path_to_list(keys, values)


'''
HOG
'''

X = tf.placeholder(tf.float32, [None, 160*96])
X_img = tf.reshape(X, [-1, 160, 96, 1])
print('X_img.shape ; ',X_img.shape)
Y = tf.placeholder(tf.float32, [None, 2])

W1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev=0.01))
L1 = tf.nn.conv2d(X_img, W1, strides=[1, 1, 1, 1], padding='SAME')
print('L1.shape : ',L1.shape)
L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
print('L1.shape : ',L1.shape)
L1 = tf.nn.relu(L1)
print('L1.shape : ',L1.shape)

W2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev=0.01))
L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')
print('L2.shape : ',L2.shape)
L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
print('L2.shape : ',L2.shape)
L2 = tf.nn.relu(L2)
print('L2.shape : ',L2.shape)

L2 = tf.reshape(L2, [-1, 7*7*64])
print('L2.shape : ',L2.shape)

W3 = tf.Variable(tf.random_normal([7 * 7 * 64, 10], stddev=0.01))
b = tf.Variable(tf.random_normal([10], stddev=0.01))
logits = tf.matmul(L2, W3) + b
print('logits.shape : ',logits.shape)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=Y))
optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

training_epochs = 20
batch_size = 20

for epoch in range(training_epochs):
    avg_cost = 0

    my_total_batch = (int)(math.ceil(train_data.size() / batch_size))

    for i in range(my_total_batch):
        my_batch_xs, my_batch_ys = train_data.next_batch(batch_size)

        c, _ = sess.run([cost, optimizer], feed_dict={X: my_batch_xs, Y: my_batch_ys})
        avg_cost += c

    print('Epoch %04d. ' % epoch, ' cost: %.f' % avg_cost )

print('Learning Finished!')

train_data.clear()

print('Test start!')

import random

# Test model and check accuracy
correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
feed_dict={X: test_data.images() , Y: test_data.labels()}
print('Accuracy:', sess.run(accuracy, feed_dict=feed_dict))

