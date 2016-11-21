import numpy as mnp
import cv2
import os 
import math
from PIL import Image


"""
Red : prediction
Blue: anser
"""
POINTSIZE = 50
# Define the codec and create VideoWriter object
path_dir = "./images/"
pred_img = Image.open("point.png")
ans_img =  Image.open("pointans.png")


ans_img = ans_img.resize((POINTSIZE,POINTSIZE))
pred_img = pred_img.resize((POINTSIZE,POINTSIZE))

teacherCodinate = []
predCodinate = []
with open('./0511teacherSignal.txt') as f:
    for line in f:
        line = line.rstrip()
        l = line.split()
        teacherCodinate.append(l)


with open('./0511pred.txt') as f_pred:
    for line_pred in f_pred:
        line_pred = line_pred.rstrip()
        l_pred = line_pred.split()
        predCodinate.append(l_pred)
print len(teacherCodinate), len(predCodinate)




k = 0
for i in teacherCodinate:
        filename = path_dir+i[0]
        print filename
        #print os.path.exists(filename)
        if (os.path.exists(filename) != True):
            continue
        image = Image.open(filename)
        for pred in predCodinate:
            match = pred
            if(i[0] == pred[0]):
                break    
        #paste points to each frame
        print i
        image.paste(ans_img,(int(i[1]),int(i[2])))
        image.paste(pred_img,(int(match[1]),int(match[2])))
        print i[1],i[2]
        print match[1],match[2]
        image.save("./pastedimages/" + '%06d.jpg' % k)
        k += 1
        """
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        """
                


"""




    # write the frame
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
f.close()
f_pred.close()

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()
"""