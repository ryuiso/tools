import numpy as mnp
import cv2
import os 
import math

import glob
import subprocess
import sys


cmd = 'ffmpeg -r 10 -i ' \
      + 'pasetedimages/%06d.jpg -r 10 -vcodec libx264 ' \
      + 'out.mp4'
print cmd
subprocess.call(cmd, shell=True)


"""ffmpeg -r 10 -i pastedimages/%06d.jpg -r 10 -vcodec libx264 foo.mp4"""




