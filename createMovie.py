import numpy as mnp
import cv2
import os 
import math


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
path_dir = "/media/ii-lab/SSD_1TB/rythmique/20160817/2agedClass/images/"
f = open("./train.txt")
for line in f:
    line = line.rstrip()
    l = line.split()
    filename = path_dir+l[0]
   	frame = cv2.imread(filename)

        # write the frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release everything if job is finished
out.release()
cv2.destroyAllWindows()