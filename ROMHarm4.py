#This code imports the necessary modules.

import random
import os
from PIL import Image 
import time
import playsound

snglst = ["C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop.mp3", "C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop2.mp3", "C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop3.mp3", "C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop4.mp3", "C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop5.mp3", "C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop6.mp3",]

srchstr = 'C:\\Users\\mysti\\Media_Files\\Dreams'

contenttot= []

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".jpg"):

            tim = os.path.getctime(filepath)

            contentdat[filepath] = tim

            contenttot.append(filepath)

totlen = len(contenttot)

totch = random.randrange(totlen)

fitch = contenttot[totch]

fich = str(contentdat[fitch])

print(fich)

finlst = []

for ctr in range(30):
 
    sublst = []

    for elem in range(totlen):
        tesstr = contenttot[elem]
        testr = str(contentdat[tesstr])
        piv2str = testr[-10:-8]

        #As y and a cause endless replication, they are like a virus, and the program learns entropy by avoiding them

        if piv2str in fich:
            sublst.append(tesstr)

    if len(sublst) > 1:        

        fich = sublst[-1]

        finlst.append(sublst)

    if len(sublst) <= 1:

        totch = random.randrange(totlen)

        fich = contenttot[totch]

        finlst.append(fich)


for elem in finlst:

    ellen = len(elem)
    im = random.randrange(ellen)

    dream = elem[im]

    img = Image.open(dream)
    
    img.show() 

    jkbx = random.randrange(6)

    songch = snglst[jkbx]

    playsound.playsound(songch, True)
        

## THE GHOST OF THE SHADOW ##
