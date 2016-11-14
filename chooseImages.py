import csv
import sys
import math
import random

GAZEX = 2
GAZEY = 3
TIME = 1
FPS = 25
args = sys.argv
timeList = []
imageList = []
if(len(args) != 2):
    print (len(args))
    print ("illegal num of argments")
    sys.exit()
f = open(args[1], 'r')

imageNmae = []
gazex = []
gazey = []
line = []
dataReader = csv.reader(f)
header = next(dataReader) #pass the headder
for row in dataReader:
    #print (row,"\n")
    if (row[GAZEY] != ''):
        timeList.append(row[TIME])
        #print (row[TIME])
        index = round(float(row[TIME])*FPS/1000)
        index = "{0:06d}".format(index)
        index = str(index).zfill(6)
        imageNmae.append(str(index) + ".jpg")
        gazex.append(str(row[GAZEX]))
        gazey.append(str(row[GAZEY]))
        line.append(index +'.jpg '+ str(row[GAZEX]) + ' ' + str(row[GAZEY])+"\n")
#print(imageList)
#print ("\n")
random.shuffle(line)


with open("train.txt", 'w') as f_out:
    for s in line:
        f_out.write(s)
        #print (i,end="")

f.close()