from scipy import misc
import glob
import matplotlib.pyplot as plt
import cv2
import random


list_train_neg = glob.glob("../train_neg/*")
list_train_neg.sort()
print(list_train_neg)

prefix = "../Data/INRIAPerson/train_64x128_H96/neg_cropped/"
image_size = [160, 96]

for filename in list_train_neg:
    image = misc.imread(filename, mode='RGB')
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(type(image))
    print(image.shape)
    plt.imshow(image)
    #plt.imshow(gray, cmap='gray')
    #reshape =
    #print(gray)

    shape = image.shape
    print(shape[0])
    print(shape[1])

    y = random.randrange(0, shape[0] - image_size[0])
    x = random.randrange(0, shape[1] - image_size[1])

    cropped = image[y:y+image_size[0], x:x+image_size[1], ]

    image_file = filename[filename.rfind('/')+1:]

    misc.imsave(prefix+image_file, cropped)

    plt.imshow(cropped)
    #plt.show()

