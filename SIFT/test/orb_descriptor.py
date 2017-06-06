import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":

    img1 = cv2.imread('/home/yildbs/box.png', 0)  # queryImage
    img2 = cv2.imread('/home/yildbs/box_in_scene.png', 0)  # trainImage

    # Initiate SIFT detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1, des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw first 10 matches.
    img3 = np.array([])
    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], img3, flags=2)

    #plt.imshow(img3), plt.show()
    cv2.imshow('aaa', img3)
    cv2.waitKey(0)

'''
    img = cv2.imread('/home/yildbs/Data/INRIA/Train_original/pos/crop001164.png')
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(gray,None)
    img = cv2.drawKeypoints(gray,kp,img)
    cv2.imshow('img', img)
    cv2.waitKey(0)
'''
