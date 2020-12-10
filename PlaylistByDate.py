#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

time = ("".join(list))

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

srchstr = 'E:\\OriginalAudio\\Songs'

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav") or filepath.endswith(".mp3") :

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

newply = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    newply.append(w)

ounam = "DateOrderedPlaylist_" + time + ".m3u"

outfile = open(ounam, "w")

for elem in newply:
     outfile.write(elem + '\n')

outfile.close()




        

## THE GHOST OF THE SHADOW ##
