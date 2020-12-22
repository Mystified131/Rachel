#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
import re
from nltk import tokenize

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

time = ("".join(list))
   
#srchstr = "C:\\Users\\mysti\\Desktop\Bin\\02_NewPoems"

srchstr = "C:\\Users\\mysti\\Desktop\\Bin\\Texts"

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

wdlst = []

for docnam in finlst:

    sublst = []

    par = ""

    with open(docnam, "r") as f:
        par = f.read()

    sublst = par.split()

    for elem in sublst:

        elem2 = elem.strip()

        if elem2[0] != "." and elem2[0] != "!" and elem2[0] != "?":

            wdlst.append(elem2)

subl = []

bigl = []

sennum = 0

for elem in wdlst:
    if len(subl) > 0:
        subl.append(elem)
    if len(subl) == 0:
        elem2 = elem[0].upper() + elem[1:]
        subl.append(elem2)

    if elem.endswith(".") or elem.endswith("!") or elem.endswith("?") :
        bigl.append(subl)
        sennum += 1
        parran = random.randrange(5)
        if parran > 3 and sennum > 4 and len(subl) > 4:
            bigl.append('\n')
            bigl.append('\n')
            sennum = 0
        subl = []

ctr = len(bigl)

lim = ctr - 5

polst = []

for x in range (ctr):
    lin = random.randrange(lim)

    rem = random.randrange(1,3)

    for y in range(rem):

        polst.append(bigl[lin + y])

    polst.append("")

bigstr = ""

for elem in polst:
    for elem2 in elem:
        if elem != '\n':
            bigstr += elem2 + " "
        if elem == '\n':
            bigstr += elem2 


ounm = "Prosaic_Dream_" + time + ".txt"

oun = "Prosaic Dream " + time 

outfile = open(ounm, "w")

outfile.write(oun + '\n')

outfile.write( '\n')

outfile.write(bigstr + '\n')

outfile.close()       

print("")

print("Your document is saved in the same folder as this code.")

## THE GHOST OF THE SHADOW ##