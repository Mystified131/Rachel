#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

time = ("".join(list))
   

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

#srchstr = 'E:\\OriginalAudio\\Songs'

srchstr =  "E:\\Visual\\VariousImages"

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".jpg") or filepath.endswith(".png") or filepath.endswith(".bmp"):

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

newply = []

newplyd = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    newply.append(w)
    newplyd.append(contentdat[w])

totlen = len(newply)

totch = random_number(totlen)

fitch = newply[totch]

fich = str(newplyd[totch])

finlst = []

for ctr in range(30):
 
    sublst = []

    for elem in range(totlen):
        tesstr = newply[elem]
        testr = str(newplyd[elem])
        piv2str = testr[-10:-8]

        if piv2str in fich:
            sublst.append(tesstr)

    if len(sublst) > 1:   

        subl = len(sublst)    

        trok = random_number(subl) 

        fich = sublst[trok]

        finlst.append(fich)

    if len(sublst) <= 1:

        totch = random_number(totlen)

        fich = newply[totch]

        finlst.append(fich)

ounam = "DreamOrderedPlaylist_" + time + ".xspf"

outfile = open(ounam, "w")

outfile.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')

outfile.write('<playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">' + '\n')

outfile.write('        <title>Playlist</title>' + '\n')

outfile.write('        <trackList>' + '\n')

for elem in finlst:
    outfile.write('                <track>' + '\n')
    outfile.write('                        <location>file:///' + elem + '</location>'+ '\n')
    outfile.write('                        <duration></duration>' + '\n')
    outfile.write('                        <extension application="http://www.videolan.org/vlc/playlist/0">' + '\n')
    outfile.write('                                <vlc:id>0</vlc:id>' + '\n')
    outfile.write('                        </extension>' +'\n')
    outfile.write('                </track>' + '\n')


outfile.write('        </trackList>'+ '\n')

outfile.write('        <extension application="http://www.videolan.org/vlc/playlist/0">' + '\n')

outfile.write('               <vlc:item tid="0"/>' + '\n')

outfile.write('        </extension>' + '\n')

outfile.write('</playlist>'+ '\n')


outfile.close()
   

## THE GHOST OF THE SHADOW ##
