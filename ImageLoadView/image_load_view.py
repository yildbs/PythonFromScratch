from scipy import misc
import glob
import matplotlib.pyplot as plt

import cv2 as cv2


#image = misc.imread("../Data/")

#pos_list = open('../pos.lst')
#print(pos_list.readline())

list_train_pos = glob.glob("../train_pos/*")
list_train_pos.sort()
print(list_train_pos)

for filename in list_train_pos:
    image = misc.imread(filename, mode='RGB')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(image.shape)
    plt.imshow(image, cmap='gray')
    plt.imshow(gray, cmap='gray')
    #reshape =
    print(gray)

