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

#srchstr = 'E:\\OriginalAudio\\Songs'

#srchstr = 'C:\\Users\\mysti\\Downloads'

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

srchstr = "TT.m3u"

content = []

finlst = []

infile = open(srchstr, "r")

plist = infile.readline()

while plist:
    content.append(plist.strip())
    plist = infile.readline()

infile.close()

leng = len(content)

for y in range(50):
 
    trk = random.randrange(leng - 12)

    skip = random.randrange(1, 12)

    adnum = trk + skip

    dreamcrack = random.randrange(9)
    if dreamcrack < 4:
        adnum = random.randrange(1,len(content))

    adstr = content[adnum]

    finlst.append(adstr)

ounam = "DreamOrderedPlaylist_" + time + ".m3u"

outfile = open(ounam, "w")

for elem in finlst:
     outfile.write(elem + '\n')

outfile.close()




        

## THE GHOST OF THE SHADOW ##
