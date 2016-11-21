import numpy as mnp
import cv2
import os 
import math


f = open("/media/ii-lab/SSD_1TB/rythmique/20160511/3agedClass/train.txt",'r')
f_out = open("./0511teacherSignal.txt",'w')
prev = "init"
for line in f:
    print prev[:10], line[:10]    
    if prev[:10] != line[:10]:
        print "a"
        f_out.write(line)
    prev = line
f_out.close()
f.close()