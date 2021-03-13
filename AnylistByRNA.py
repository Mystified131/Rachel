#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2

#this code retrieves the date and time from the computer, to create the timestamp

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
        ctr = random_number(24)
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

newlst = []

startlen = random_number(leng -50)

for x in range(startlen, (startlen + 50)):
    newlst.append(x)

fonlst = remaplist(newlst)

finlst = [] 

for y in range(len(fonlst)):
    valu = fonlst[y]
    if valu > leng:
        valu -= random_number(leng)
    finlst.append(content[valu])

ounam = "DreamOrderedPlaylist_" + time + ".m3u"

outfile = open(ounam, "w")

for elem in finlst:
     outfile.write(elem + '\n')

outfile.close()
    

## THE GHOST OF THE SHADOW ##
