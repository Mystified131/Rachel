#This code imports the necessary modules.

import random
import os
from collections import defaultdict

srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav") or filepath.endswith(".mp3") :

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

newply = []

for w in sorted(contentdat, key=contentdat.get, reverse=True):
    newply.append(w)


outfile = open('DateOrderedPlaylist.m3u', "w")

for elem in newply:
     outfile.write(elem + '\n')

outfile.close()




        

## THE GHOST OF THE SHADOW ##
