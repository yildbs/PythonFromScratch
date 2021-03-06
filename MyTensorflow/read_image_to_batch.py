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
        self._num_label = 2

    def clear(self):
        self._data_image.clear()
        self._data_label.clear()
        self._is_gray_image = True
        self._shape = 0
        self._batch_count = 0


    def set_num_label(self, value):
        self._num_label = value

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

    def add_image_path_to_list(self, image_paths, labels):
        #image = misc.imread(image_path, False, 'RGB')
        #if self._is_gray_image:
#            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        for image_path in image_paths:
            image = misc.imread(image_path, True, 'F')
            image = image / 255.
            self._shape = image.shape
            reshaped = np.reshape(image, (image.size))
            self._data_image.append(np.asarray(reshaped))

        for label in labels:
            label_one_hot =  np.zeros([self._num_label])
            label_one_hot[int(label)] = 1
            self._data_label.append(np.asarray(label_one_hot))

    def next_batch(self, batch_size):
        #if self._batch_count >= len(self._data_image):
        #    return None, None

        start = self._batch_count
        end = start + batch_size
        self._batch_count = end

        if end >= len(self._data_image):
            end = len(self._data_image)
            self.reset()

        return self._data_image[start:end], self._data_label[start:end]
