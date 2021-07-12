#This code imports the necessary modules.

import random
import os
from PIL import Image, ImageOps, ExifTags
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

#srchstr = "F:\BlackAndWhitePhotography"

srchstr = "F:\\Visual\\VisualArt\\PrintsThatAreUseful\\jpg"

contenttot= []

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".jpg") or filepath.endswith(".JPG"):

            tim = os.path.getctime(filepath)

            contentdat[filepath] = tim

            contenttot.append(filepath)

finlst = []

for ctr in range(30):

    totlen = len(contenttot)

    x2 = random_number(totlen)

    finlst.append(contenttot[x2])

    contenttot.remove(contenttot[x2])

for elem in finlst:

    img = Image.open(elem)

    img = ImageOps.exif_transpose(img) 
    
    img.show() 

    time.sleep(10)

    #os.system("taskkill /im firefox.exe /f")
    os.system("taskkill /im Chrome.exe /f")
    #os.system("killall -9 'Google Chrome'")

    #jkbx = random.randrange(6)

    #songch = snglst[jkbx]

    #playsound.playsound(songch, True)
        

## THE GHOST OF THE SHADOW ##
