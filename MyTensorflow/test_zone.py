# Lab 11 MNIST and Convolutional Neural Network
import tensorflow as tf
import random
# import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets("../Data/MNIST_data/", one_hot=True)


batch_xs, batch_ys = mnist.train.next_batch(20)

print(batch_xs.shape)
print(type(batch_xs))
print(batch_ys.shape)
print(type(batch_ys))
