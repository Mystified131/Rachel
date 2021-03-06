#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
import re
from unidecode import unidecode

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

time = ("".join(list))
   
srchstr = "C:\\Users\\mysti\\Desktop\Bin\\02_NewPoems"

srchstr = "C:\\Users\\mysti\\Desktop\\Bin\\Matt"

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".txt") :

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

newply = []

newplyd = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    newply.append(w)
    newplyd.append(contentdat[w])

totlen = len(newply)

totch = random.randrange(totlen)

fitch = newply[totch]

fich = str(newplyd[totch])

finlst = []

for ctr in range(50):
 
    sublst = []

    for elem in range(totlen):
        tesstr = newply[elem]
        testr = str(newplyd[elem])
        piv2str = testr[-10:-8]

        if piv2str in fich:
            sublst.append(tesstr)

    if len(sublst) > 1:   

        subl = len(sublst)    

        trok = random.randrange(subl) 

        fich = sublst[trok]

        finlst.append(fich)

    if len(sublst) <= 1:

        totch = random.randrange(totlen)

        fich = newply[totch]

        finlst.append(fich)

txlst = []

for docnam in finlst:

    infile = open(docnam, "r")

    plist = infile.readline()
    while plist:
        if len(plist) > 3:
            qlist = plist.strip()
            tlist = qlist.replace(')', '')
            ulist = tlist.replace('(', '')
            rlist = ulist[0].lower() + ulist[1:]
            slist = unidecode(rlist)
            txlst.append(slist)
        plist = infile.readline()
    infile.close()
  
ctr = int(len(txlst)/5)

lim = ctr - 5

polst = []

for x in range (ctr):
    lin = random.randrange(lim)

    rem = random.randrange(2,4)

    for y in range(rem):

        polst.append(txlst[lin + y])

        polst.append("")

    #polst.append("")

ounm = "Poetic_Dream_" + time + ".txt"

oun = "Poetic Dream " + time 

outfile = open(ounm, "w")

outfile.write(oun + '\n')

outfile.write( '\n')

outfile.write( '\n')

for elem in polst:

    outfile.write(elem + '\n')

outfile.close()       

print("")

print("Your document is saved in the same folder as this code.")

## THE GHOST OF THE SHADOW ##