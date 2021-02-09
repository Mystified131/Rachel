#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
#from itertools import permutations

def permutList(l):
    if not l:
            return [[]]
    res = []
    for e in l:
            temp = l[:]
            temp.remove(e)
            res.extend([[e] + r for r in permutList(temp)])

    return res

def remaplist(lst):
    rnalst = []
    l4 = max(lst)
    l1 = int(l4 / 4)
    l2 = int(l4 / 2)
    l3 =  l1 + l2
    rnalst.append(l1)
    rnalst.append(l2)
    rnalst.append(l3)
    rnalst.append(l4)
    rnatot = (permutList(rnalst))
    x = len(lst)
    y = (x // 4) + 1
    outlst = []
    for z in range(y):
        ctr = random.randrange(24)
        addlst = rnatot[ctr]
        outlst.append(addlst)
    finlst = []
    for elem in outlst:
        for elem2 in elem:
            if len(finlst) <= x:
                finlst.append(elem2)
    fonlst = []
    for a in range(x):
        val = (lst[a] + finlst[a])
        fonlst.append(val)
    return fonlst

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

time = ("".join(list))
   

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

srchstr = 'E:\\OriginalAudio\\Songs'

#srchstr = 'C:\\Users\\mysti\\Downloads'

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav") or filepath.endswith(".mp3") :

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

newply = []

newplyd = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    newply.append(w)
    newplyd.append(contentdat[w])

totlen = len(newply)

newlst = []

startlen = random.randrange(totlen -100)

for x in range(startlen, startlen + 100, 2):
    newlst.append(x)

fonlst = remaplist(newlst)

finlst = [] 

for y in range(50):
    valu = fonlst[y]
    if valu > totlen:
        valu -= totlen
    finlst.append(newply[valu])
  

ounam = "DreamOrderedPlaylist_" + time + ".m3u"

outfile = open(ounam, "w")

for elem in finlst:
     outfile.write(elem + '\n')

outfile.close()




        

## THE GHOST OF THE SHADOW ##
