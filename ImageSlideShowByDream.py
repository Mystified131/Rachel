#This code imports the necessary modules.

import random
import os
from PIL import Image, ExifTags
import time
import playsound
from RandFunct import random_number
from RandFunct2 import random_number2

snglst = ["F:\\OriginalAudio\\Songs\\SongsC\\Bonegenb\\BoneGen1.wav",
"F:\\OriginalAudio\\Songs\\SongsC\\Bonegenb\\BoneGen2.wav",
"F:\\OriginalAudio\\Songs\\SongsC\\Bonegenb\\BoneGen3.wav",
"F:\\OriginalAudio\\Songs\\SongsC\\Bonegenb\\BoneGen4.wav",
"F:\\OriginalAudio\\Songs\\SongsC\\Bonegenb\\BoneGen5.wav",
"F:\\OriginalAudio\\Songs\\SongsC\\Bonegenb\\BoneGen6.wav",
"F:\\OriginalAudio\\Songs\\SongsC\\Bonegenb\\BoneGen7.wav",
"F:\\OriginalAudio\\Songs\\SongsC\\Bonegenb\\BoneGen8.wav",
"F:\\OriginalAudio\\Songs\\SongsC\\Bonegenb\\BoneGen9.wav",
"F:\\OriginalAudio\\Songs\\SongsC\\Bonegenb\\BoneGen10.wav"]

#snglst = ["C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop.mp3", "C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop2.mp3", "C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop3.mp3", "C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop4.mp3", "C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop5.mp3", "C:\\Users\\mysti\\Media_Files\\Dreams\\DreamHop6.mp3",]

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Dreams'

#srchstr = "C:\\Users\\mysti\\Coding\\Rachel\\static"

srchstr = "F:\BlackAndWhitePhotography"

contenttot= []

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".jpg") or filepath.endswith(".JPG"):

            tim = os.path.getctime(filepath)

            contentdat[filepath] = tim

            contenttot.append(filepath)

totlen = len(contenttot)

totch = random_number(totlen)

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

    try:

        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
             break
    
        exif = img._getexif()

        if exif[orientation] == 3:
            img=img.rotate(180)#, expand=True)
        elif exif[orientation] == 6:
            img=img.rotate(270)#, expand=True)
        elif exif[orientation] == 8:
            img=img.rotate(90)#, expand=True)

    except:

        print()

    
    img.show() 

    jkbx = random.randrange(6)

    songch = snglst[jkbx]

    playsound.playsound(songch, True)
        

## THE GHOST OF THE SHADOW ##
