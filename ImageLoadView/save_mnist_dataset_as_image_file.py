from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as misc

saveTrain = False # True : save train image, False : save test image

mnist = input_data.read_data_sets("../Data/MNIST_data/", one_hot=False)

batch_size = 1

if saveTrain:
    total_batch = int(mnist.train.num_examples / batch_size)
else:
    total_batch = int(mnist.test.num_examples / batch_size)

print("total_batch : " , total_batch)

if saveTrain:
    fLabel = open('../Data/MNIST_data_raw/label_train.txt','w')
else:
    fLabel = open('../Data/MNIST_data_raw/label_test.txt', 'w')

for i in range(total_batch):

    if saveTrain:
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
    else:
        batch_xs, batch_ys = mnist.test.next_batch(batch_size)

    reshaped = np.reshape(batch_xs, (28,28))

    if saveTrain:
        filename = '../Data/MNIST_data_raw/train/train_%06d.jpg'% i
    else:
        filename = '../Data/MNIST_data_raw/test/test_%06d.jpg' % i

    misc.imsave(filename, reshaped)

    if saveTrain:
        filename_in_label = 'train/train_%06d.jpg' % i
    else:
        filename_in_label = 'test/test_%06d.jpg' % i

    #print(batch_ys[0])
    line = filename_in_label + '  ' + str(batch_ys[0]) + '\n'
    fLabel.write(line)

    #print(batch_xs.shape)
    #print(reshaped.shape)
    #print(batch_ys.shape)

    #if(i==20) :
    #    break
    print("saved at ", i)


fLabel.close()