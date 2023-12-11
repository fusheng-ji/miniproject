import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

if __name__ == "__main__":
    img1 = cv.imread('datasets/object_level/OminiObject3D/blender_renders_24_views/book/book_002/008.png', cv.IMREAD_GRAYSCALE)  #queryimage # left image
    img2 = cv.imread('datasets/object_level/OminiObject3D/blender_renders_24_views/book/book_002/010.png', cv.IMREAD_GRAYSCALE) #trainimage # right image
    
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    
    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)
    pts1 = []
    pts2 = []
    
    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.8*n.distance:
            pts2.append(kp2[m.trainIdx].pt)
            pts1.append(kp1[m.queryIdx].pt)
    pts1 = np.int32(pts1)
    pts2 = np.int32(pts2)
    F, mask = cv.findFundamentalMat(pts1,pts2,cv.FM_LMEDS)
  
    # Stereo rectification (uncalibrated variant)
    h1, w1 = img1.shape
    h2, w2 = img2.shape
    _, H1, H2 = cv.stereoRectifyUncalibrated(
        np.float32(pts1), np.float32(pts2), F, imgSize=(w1, h1)
    )
    # rectify the images
    img1_rectified = cv.warpPerspective(img1, H1, (w1, h1))
    img2_rectified = cv.warpPerspective(img2, H2, (w2, h2))
    fig, axes = plt.subplots(1, 4, figsize=(15, 10))
    
    axes[0].imshow(img1, cmap="gray")
    axes[0].set_title("First view")
    axes[1].imshow(img1_rectified, cmap="gray")
    axes[1].set_title("First view rectified")
    axes[2].imshow(img2_rectified, cmap="gray")
    axes[2].set_title("Second view rectified")
    axes[3].imshow(img2, cmap="gray")
    axes[3].set_title("Second view")
    # parallel line
    axes[1].axhline(250)
    axes[2].axhline(250)
    axes[1].axhline(450)
    axes[2].axhline(450)

    plt.suptitle("Rectified images")
    plt.show()