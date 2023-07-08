import cv2
import matplotlib.pyplot as plt

vidcap = cv2.VideoCapture('fire.mov')
success, image = vidcap.read()
print(success, 'hehe')
# Note that frameNumber 1 in the annotation is frame index 0s
count = 1
count = 0

amount_of_frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
print(amount_of_frames)

while success:
  cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success, count)
  count += 1