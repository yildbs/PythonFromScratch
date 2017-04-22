from scipy import misc
import numpy as np
import cv2


class MyData:
    def __init__(self):
        self._is_gray_image = True
        self._data_image = []
        self._data_label = []
        self._shape = 0
        self._batch_count = 0

    def clear(self):
        self._data_image.clear()
        self._data_label.clear()
        self._is_gray_image = True
        self._shape = 0
        self._batch_count = 0

    def images(self):
        return self._data_image[0:-1]

    def labels(self):
        return self._data_label[0:-1]

    def reset(self):
        self._batch_count = 0

    def size(self):
        return len(self._data_image)

    def is_gray_image(self, value):
        self._is_gray_image = value

    def add_image_path_to_list(self, image_path, label):
        #image = misc.imread(image_path, False, 'RGB')
        #if self._is_gray_image:
#            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = misc.imread(image_path, True, 'F')
        image = image / 255.
        self._shape = image.shape

        reshaped = np.reshape(image, (image.size))
        label_one_hot =  np.zeros([10])
        label_one_hot[int(label)] = 1

        self._data_image.append(np.asarray(reshaped))
        self._data_label.append(np.asarray(label_one_hot))

    def next_batch(self, batch_size):
        if self._batch_count >= len(self._data_image):
            return None, None

        start = self._batch_count
        end = start + batch_size

        if end > len(self._data_image):
           end = len(self._data_image)

        self._batch_count = end
        return self._data_image[start:end], self._data_label[start:end]
