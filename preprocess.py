# now we have frames of videos

# we need to convert them to grayscale


import cv2
import matplotlib.pyplot as plt
import numpy as np
# reading a single image

import glob
cv_img = []
count = 0
for img in glob.glob("frames/*.jpg"):
    file = img
    # read image
    img = cv2.imread(img)
    hh, ww = img.shape[:2]



    # define circles
    radius1 = 200
    xc = int(1950/2)
    yc = int(1250/2)

    # draw filled circles in white on black background as masks
    mask1 = np.zeros_like(img)
    mask1 = cv2.circle(mask1, (xc,yc), radius1, (255,255,255), -1)
    mask = mask1

    # put mask into alpha channel of input
    result = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    result[:, :, 3] = mask[:,:,0]

    crop = result[yc-radius1:yc+radius1, xc-radius1:xc+radius1,]

    height, width = crop.shape[:2]
    center = (width/2, height/2)
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=-50, scale=1)
    rotated_image = cv2.warpAffine(src=crop, M=rotate_matrix, dsize=(width, height), borderMode=cv2.BORDER_CONSTANT, borderValue=(255,255,255))
    
    
    # COVERTING TO GRAYSCALE
    gray = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2GRAY)

    #ret, thres = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

    # save results
    #cv2.imwrite('lena_masks.png', mask)
    path = 'preprocessed/' + str(file)
    #print(path)
    cv2.imwrite(path, gray)
    count += 1
    print('count: ', count, end='\r')

    img_row_sum = np.sum(gray,axis=1).tolist()

    if count>20:
        break

    # plt.plot(img_row_sum)
    # plt.show()

